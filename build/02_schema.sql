create table bills (
  id uuid primary key default gen_random_uuid(),
  code text unique not null,                    -- 4 chars from ABCDEFGHJKMNPQRSTUVWXYZ23456789
  restaurant_name text not null default 'Dinner',
  mode text not null default 'items' check (mode in ('items','even','wheel')),
  status text not null default 'claiming' check (status in ('claiming','locked','settled')),
  host_name text,
  host_monzo text,
  host_revolut text,
  host_sort_code text,
  host_account_number text,
  wheel_winner_id uuid,
  wheel_spun_at timestamptz,
  wheel_pay_to text not null default 'waiter' check (wheel_pay_to in ('waiter','host')),
  settled_at timestamptz,
  created_at timestamptz not null default now()
);

create table receipts (                          -- "rounds"; Phase A creates exactly one
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade,
  label text not null default 'Round 1',
  position int not null default 1,
  service_mode text not null default 'add' check (service_mode in ('none','add','included')),
  service_rate numeric not null default 0.125,
  service_included_pence int not null default 0,
  receipt_total_pence int,
  discount_pence int
);

create table items (
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade,
  receipt_id uuid not null references receipts(id) on delete cascade,
  name text not null,
  price_pence int not null check (price_pence >= 0), -- one unit; quantities exploded into rows
  position int not null default 0
);

create table guests (
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade,
  name text not null,
  emoji text not null default '🍽️',
  color text not null default 'oklch(0.52 0.22 262)',
  is_host boolean not null default false,
  has_phone boolean not null default true,
  in_wheel boolean not null default true,          -- opt-out (v3.1)
  paid_at timestamptz,
  created_at timestamptz not null default now()
);

create table claims (
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade,
  item_id uuid not null references items(id) on delete cascade,
  guest_id uuid not null references guests(id) on delete cascade,
  created_at timestamptz not null default now(),
  unique (item_id, guest_id)
);

-- Realtime; REPLICA IDENTITY FULL so DELETE events still carry bill_id for filtering
alter table bills replica identity full;   alter table receipts replica identity full;
alter table items replica identity full;   alter table guests replica identity full;
alter table claims replica identity full;
alter publication supabase_realtime add table bills, receipts, items, guests, claims;

-- No accounts by design: anon read/write, tables reachable only via their code
alter table bills enable row level security;    create policy "public" on bills    for all using (true) with check (true);
alter table receipts enable row level security; create policy "public" on receipts for all using (true) with check (true);
alter table items enable row level security;    create policy "public" on items    for all using (true) with check (true);
alter table guests enable row level security;   create policy "public" on guests   for all using (true) with check (true);
alter table claims enable row level security;   create policy "public" on claims   for all using (true) with check (true);

-- D2 clean-up (Claude runs it by hand tonight; a scheduled job later)
create or replace function cleanup_old_tables() returns int language sql as $$
  with d as (delete from bills
             where (status = 'settled' and settled_at < now() - interval '7 days')
                or created_at < now() - interval '30 days' returning 1)
  select count(*)::int from d;
$$;
