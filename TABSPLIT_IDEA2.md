# 🧾 Idea 2: TabSplit (Ready-to-Build Spec, v3)
**Theme:** Split a group restaurant bill item by item (or evenly, or spin for it), and get the host paid before anyone stands up  
**Role in Hackathon:** ✅ The chosen build (SoftCircle, in `SOFTCIRCLE_IDEA1.md`, is the backup)  
**When:** **today, 28 Oct 2026, 18:00–22:00** | **Event:** Lovable Buildathon, Imperial Entrepreneurs x YFL  
**Spec owner:** Claude (lead) · Product decisions: Faizan · Critic: Argon 🔍

> **This file is the single source of truth for the build.** A new session (Claude, Argon or a teammate) should be able to build TabSplit from this file alone.  
> **History:** v1 = Gemini's proposal (git history) · v2 = Claude's rewrite + research · v2.1 = Argon review round 1 (§15) · **v3 = Faizan's product decisions (joining by code/link, two-step guest screen, multi-photo receipts, rounds, split evenly, spin the wheel, the full payment flow) + test-run results.** · **v3.1 = Argon review round 2 applied (§16).** · **v3.2 = Argon review round 3 of the build kit + mockups applied (§17).**

---

## 0. Decisions Log

### Confirmed by Faizan (v3)
| # | Decision |
|---|---|
| D1 | **Join by link, 4-character code or QR.** At a real table the host shares a link in the group chat or people type a code (Kahoot-style). The QR is mostly for the stage demo. Code = **4 characters, letters + digits**, no look-alikes (0/O, 1/I/L): ~920,000 combinations. |
| D2 | **Tables are deleted** 7 days after they're settled, or after 30 days if they never settle. The code is then free to reuse. |
| D3 | **Guest flow is two steps:** **Pick** (tap what you ate) → **Continue** → **Table** (everyone and what they claimed). Unclaimed items are *not* listed again on the Table step: a **pill** at the top shows "3 unclaimed · £14.50", and tapping it expands them. |
| D4 | **The host's phone is the host screen.** The projector view is a separate **Big screen mode** used for the pitch. If the venue won't let us plug in a phone, use the MacBook's iPhone Mirroring. |
| D5 | **The host enters payment details once:** Monzo username, Revolut tag, and/or sort code + account number. All optional. Guests only ever see buttons. |
| D6 | **One link per table, for everything:** joining, claiming, paying, and paying later. No accounts. Phones remember who you are, and on a new phone you pick your name. |
| D7 | **Payment is confirmed by honour system + host referee.** The guest taps "I've paid", and the host can undo it or mark someone paid. We can't see anyone's bank. Automatic confirmation via Open Banking is the roadmap. |
| D8 | **Three modes:** **Split by items** (default) · **Split evenly** · **Spin the wheel** (opt-in card roulette). |
| D9 | **A receipt can have up to 4 photos** (long receipts), read as one receipt. **A table can have several receipts ("rounds")** for when the group orders again. *(v3.1: rounds are cut for tonight; the schema keeps them for later.)* |

### Added by Claude (v3), check these
| # | Addition | Why |
|---|---|---|
| C1 | **Add a person without a phone** ("Sam 🪫"), **for Split evenly and the wheel only** (v3.1: no claiming on someone else's behalf) | Every table has someone with a dead battery. In items mode, a friend claims Sam's food as their own and Sam pays them back |
| C2 | **Wheel is opt-out** (v3.1): everyone at the table is on it, with a big **"Sit this one out"** button. The **winner is chosen once and saved**, and every phone animates to the same result | Opt-in left the wheel empty on stage (Argon). Sitting out is still one visible tap, so nobody is pressured, and nobody can claim "mine landed on Tom" |
| C3 | **Wheel winner pays the waiter** by default. If the host already paid by card, the winner gets "Pay Faizan £74.93" | Covers both real situations |
| C4 | **"Who are you?" only appears after the bill is locked** (when paying later on a new phone). It lists only **unpaid, non-host** people, with **"Just watching 👀"** on top. While claiming, new phones get an instant alias | Keeps joining at zero taps, and a late scanner can't take someone's place by accident |
| C5 | **Pay buttons only appear after the host locks the bill** | Amounts keep changing while people claim |
| C6 | **Bank details only show in the app after lock** | **A UI gate only**: the data is readable through the open API. Say so if asked (§14). The real fix is pay-by-bank links, which replace raw bank details |

### Build order & pitch (Faizan: "Claude and Argon decide the build; we decide the pitch once we see a working demo")
- **Q7, build order (decided by Claude, agreed by Argon in round 2):** **A** core → **B** receipt photos → **C** modes (wheel, even, no-phone) → **D** rounds.
  - *Why photos before the wheel:* "AI reads your receipt" is the expected wow moment at a Lovable AI event, and Phase A already works without it.
  - *Escape hatch:* if B isn't working by **19:35**, stop it, keep "Use demo receipt" + "Type it in", and go straight to C. The wheel is pure frontend + realtime, so it's lower risk than the AI reader.
  - **D (rounds) is cut for tonight** (Argon: zero pitch value). The `receipts` table stays, with exactly one receipt per table.
- **Q8, pitch ending: decided on the night** (21:15, after the full loop works on 5 phones). Both §13 endings stay ready: **wheel finale** or **Settled ✅ confetti**. Argon recommends the wheel. Note: a real "everyone paid" Settled can't happen on stage, because judges won't actually pay, so the wheel (pay to waiter → Settled ✅) is the natural way to show it.

---

## 1. The Idea (One Paragraph)
When the bill comes, the host photographs the receipt (several photos if it's long) and AI turns it into a list of items. The host drops the table link in the group chat, or everyone types a 4-character code. Everyone taps what they ate, with no app, no sign-up and not even a name to type, and taps **Continue** to see the whole table: who had what, plus a pill showing what's still unclaimed. Shared dishes split automatically. The host can switch to **Split evenly** or **Spin the wheel** (one phone spins, everyone's screen spins, one person pays). When the host locks the bill, each phone shows **"You owe Faizan £23.51"** with a Monzo button (amount filled in), Revolut and bank-transfer details. People tap "I've paid", the host watches the ticks come in and chases the rest on WhatsApp with the same link. **Nobody leaves owing the host money.**

---

## 2. Competitor Reality Check (Oct 2026) & Our Honest Wedge

| Who | What they do well | Where they stop |
|---|---|---|
| **Splitwise Itemize** (free in UK since 14 Oct 2026) | 50M+ users. QR claiming with no download. Proportional tax and tip. | The host needs Splitwise. Per launch coverage, it ends with Splitwise Pay (US), cash, or **an IOU added to a running Splitwise balance**. The debt is recorded, not settled. |
| **BillMath / BillTap / Divvi / SplitterUp** | Web QR splitters with no signup | Small and generic, mostly US-centric. No UK bank links, no "who's paid" view. |
| **Monzo / Revolut split** | Real money moves instantly | They split a *transaction*, so they can't read a paper receipt line by line. Per-person amounts are typed by hand. |
| **Sunday / me&u** | QR paying straight into the till | Only in venues that bought their system. |

**Our wedge, said honestly:** *"Splitting the bill is solved. Getting paid isn't."* Splitwise turns dinner into an IOU on a ledger. TabSplit is built around the moment at the table: a shared view everyone watches fill up, UK bank payments with the amount filled in, live **paid ✅** ticks, a bill that isn't "done" until the host is whole, and **the wheel**, which nobody else has and which people share.

**Business story (keep it modest):**
1. **Growth:** every table puts TabSplit in front of ~6 people who didn't install anything. Each guest is a future host. The wheel is the shareable moment ("Tom lost the wheel again 😂").
2. **Where the money is (the bet):** today guests pay the *host*. Next, guests **pay the venue directly by bank (Open Banking pay-by-bank) from the same screen**. The venue pays lower fees than on cards and turns tables faster, and we take a cut of the saving. No POS hardware, unlike Sunday/me&u. Open Banking also gives us **automatic payment confirmation** (replacing D7's honour system).
3. **Side bet:** a paid tier for student society treasurers, who front the bill at every social.
4. **Don't claim** neobank affiliate fees, a market size, specific fee percentages, or that we're regulated. Pay-by-bank needs an FCA-authorised partner. Say "via a licensed provider".

---

## 3. Claude's Verdict
**Strengths:** the most relatable problem we have, zero jargon, a live multi-phone demo, and the wheel, a genuinely new and very visual moment.  
**Weaknesses:** Splitwise took the "first" story. The business model is a bet. The scope grew in v3, so the order of building and the feature freeze matter more.  
**Net:** build it. **Phase A alone is a complete, demo-able product.** Every later phase is a bonus that can be cut at 20:45 without breaking anything.

| | Relatable | Demo wow | No jargon | Feasibility (×2) | Business | Judge fit | **/70** |
|---|---|---|---|---|---|---|---|
| TabSplit v2 | 10 | 9 | 10 | 8 (16) | 4 | 6 | 55 |
| **TabSplit v3** | 10 | 10 | 10 | 7 (14) | 5 | 7 | **56** |

---

## 4. Features by Build Phase

### 🅰 Phase A: Core (the product works end to end). MUST
1. **Home:** **Start a table** · **Join** with a 4-char code box · **Your recent tables** (kept on this phone).
2. **Create (host), on `/new`:**
   - **Step 1 Receipt:** **Use demo receipt** (fills step 2 with the Dishoom items; the host still creates a real table, so they get host controls) or **Type it in** (manual items). Photos arrive in Phase B.
   - **Step 2 Review:** edit, delete or add items. Check line: *"Receipt says £Y, we count £X (items + service)"*. Service: **Already on receipt £__ / Add 10 / 12.5 / 15% / None**.
   - **Step 3 You:** host name, Monzo username, Revolut tag, sort code + account number (all optional) → **Open the table**.
3. **Share (host):** a **Share** button opens the phone's share sheet with *"Join our table on TabSplit: <link> (code K7Q2)"*. Also **Copy link**, a **QR** pop-up, and a **Big screen** link.
4. **Join (guest):** open the link or type the code → instantly get a **food alias + emoji** ("Garlic Naan Bandit 🧄"), renamable inline. The guest row is created **as soon as the page opens** while the table is claiming (never on `/screen`, never after lock), so aliases pop up on the big screen straight away. People who join but eat nothing show £0, and the host can remove them. Identity is kept in `localStorage`.
5. **Pick (step 1):** big item cards. Tap = claim, tap again = unclaim, several claimers = shared (÷ n shown). Others' avatars show on each item. Sticky footer: *"Your share £X (incl. £Y service)"* + **Continue →**.
6. **Table (step 2):** **pill** *"⚠ 3 unclaimed · £14.50 ▾"* (tap to expand and claim). Then **you first**, then everyone else: name, items, total. A **← Edit my items** link goes back to Pick.
7. **Live sync** of everything across phones (Supabase Realtime): debounced refetch (250ms), latest response wins, taps still saving stay layered on top, plus a refetch on reconnect and when the phone wakes.
8. **Lock (host):** a **permanent "Lock bill" button in the host's footer** (not hidden in ⚙️). It pulses when the pill hits 0: *"Everything's claimed. Lock it?"*. Locking early asks to confirm. After lock, amounts are frozen, and a tap still on its way is undone with "The bill's locked".
9. **Pay (guest, after lock):** *"You owe Faizan £23.51"* + breakdown →
   - **Pay on Monzo** (`monzo.me/<user>/<amount>?d=TabSplit <restaurant>`)
   - **Revolut** (`revolut.me/<tag>` + **Copy £23.51**)
   - **Bank transfer** (sort code, account no., reference *"TabSplit K7Q2 Priya"*, each with a copy button)
   - **I've paid ✅**

   Only methods the host filled in are shown.
10. **Track (host, after lock):** everyone with **owes ⏳ / paid ✅**. Per person: **Mark paid** (cash) / **Undo**. The host's own row says *"you paid the restaurant"*.
11. **Pay later:** reopening the link on the same phone goes straight to "You owe…". On a new phone after lock: **"Who are you?"** lists only unpaid people (not the host), plus **"Just watching 👀"**.
12. **Settled:** when `isSettled()` is true → **Settled ✅** + confetti on every phone.
13. **Big screen mode** `/t/:code/screen`: read-only, **fits exactly one screen (100vh, no scrolling)**, big QR + code, the items/people view, the progress bar, and the wheel when it spins.
14. **Demo safety:** a seeded table for testing only (it has no host, so **never demo from `/t/DEMO`**); **Reset** (host ⚙️, clears claims and payments); **Simulate table** (`?demo=1`, 4 fake guests claim with 1–2s gaps; only if the audience can't scan, and say so).

### 🅱 Phase B: Receipt Photos. MUST for the demo
15. **Add photos:** up to **4 photos per receipt** ("long receipt? add the bottom half"), read together as **one** receipt, with overlapping lines removed (§8). Photos go straight to the reader as resized JPEGs and are **never stored** (v3.1: no storage bucket).
16. **Tonight's receipt preset:** photos picked once in rehearsal and **kept on the host's phone** (localStorage, resized), then read live with one tap on stage. No camera picker on stage.
17. "Reading receipt…" state, a 20s timeout and a fallback to editing by hand. Never a dead end.

### 🅲 Phase C: Modes + People. SHOULD
18. **Mode switch (host ⚙️):** **Split by items** · **Split evenly** · **Spin for it 🎡**. Allowed before lock. After lock, switching unlocks and clears payments, with a confirm step.
19. **Split evenly:** everyone at the table (host included) owes an equal, penny-exact share of the **whole** bill. The Table step shows *"£24.98 each × 3"*.
20. **Spin the wheel:**
    - Everyone is **on the wheel by default**, with a big **Sit this one out** button. No-phone people are on it too, and the host can sit them out.
    - With ≥2 in, the host taps **Spin**. The host's phone picks the winner (`pickWinner`) and saves `wheel_winner_id` + `wheel_spun_at`.
    - **Every phone and the big screen** start the same 5-second spin **the moment they see `wheel_winner_id` change from empty to set** (via realtime), and land on the winner (`wheelRotation`, slices in `wheelOrder`, i.e. by id). **Don't time it against `wheel_spun_at`**, because phone clocks drift by seconds. A phone that *opens* after the spin shows the result straight away.
    - Result: *"🎉 Tom pays £74.93"*. If **pay to waiter** (default) → settled. If **pay to host** → Tom gets the Pay screen for the full amount (`computeWheel`), and it's settled when he pays, or straight away if the host won.
21. **Add person without a phone (host):** "+ Add Sam 🪫". **Counts in Split evenly and the wheel only**, with no claiming on their behalf (v3.1). The host can mark Sam paid.
22. **"Who had the …? 👀"** banner when 1–2 items are left. **Chase on WhatsApp** (host, after lock): `wa.me/?text=Still owed for <restaurant> 🧾 Tom £24.58 · Sam £18.20, pay here: <link>`.

### 🅳 Phase D: Rounds. ✂️ CUT for tonight (v3.1), kept for later
23. **Add another round (host):** a second (third…) receipt with its own photos and service charge. Items are grouped by round on Pick and Table. Totals come from `computeBill()` across all rounds.

### 🔵 Stretch (only if A–D are done)
24. "Say what you had": type *"the lamb and half the naans"* and AI ticks the items.
25. Discounts spread across everyone automatically (for now: the host edits prices; §8).
26. Auto-deleting tables (D2) as a scheduled job. Tonight it's a SQL function Claude runs by hand (§6).

### 🔴 Don't Build
Accounts/login · real payment processing or Open Banking · Splitwise-style running balances/history · multi-currency · VAT breakdowns · POS integration · native app/PWA · custom % splits · push notifications/email · relying on live camera reading as the only path in the demo.

---

## 5. Screens & Routes

| Route | Who | States |
|---|---|---|
| `/` | Everyone | Start a table · Join [ K7Q2 ] · Your recent tables |
| `/new` | Host | Step 1 Receipt (demo / type / photos) → Step 2 Review → Step 3 You (payment details) → creates the table → `/t/:code` |
| `/t/:code` | Everyone (role from `localStorage`) | **Claiming:** Pick ⇄ Table (items mode) · Even view · Wheel (I'm in / spin / result) → **Locked:** Pay (guest) / Track (host) → **Settled** |
| `/t/:code/screen` | Projector | Read-only big view of whatever state the table is in |

**Design:** receipt-paper off-white, ink-black text, monospace prices, one bold accent, green = claimed, pulsing red = unclaimed. Big tap targets. Mobile-first everywhere except `/screen`, which is projector-first and **must never scroll**. Add **≥72px bottom padding** on phones so Lovable's "Edit with Lovable" badge (free plan) never covers the sticky footer. Don't imitate Monzo or Revolut branding.

### Screen sketches (rendered mockups to follow)
```
GUEST · PICK                          GUEST · TABLE
┌──────────────────────────┐         ┌──────────────────────────┐
│ Dishoom · Table K7Q2      │         │ ⚠ 3 unclaimed · £14.50 ▾  │ ← tap to expand + claim
│ You: Garlic Naan Bandit 🧄 ✎│        ├──────────────────────────┤
│ ○ Chicken Ruby    F  £15.90│         │ 🧄 You           £23.51   │ ← you, pinned first
│ ● Black Daal  ÷2 P,T £9.90 │         │    Ruby · ½ Daal · Chai   │
│ ○ Lamb Biryani    T  £16.90│         │ P  Priya         £16.82   │
│ ● Garlic Naan        £4.50 │         │ T  Tom           £24.58   │
├──────────────────────────┤         │ 🥟 Momo Menace    £0.00    │
│ Your share  £23.51        │         ├──────────────────────────┤
│ incl. £2.61 service       │         │ ← Edit my items           │
│ [ Continue → ]            │         │ Waiting for Faizan to lock│
└──────────────────────────┘         └──────────────────────────┘

GUEST · PAY (after lock)              HOST · TRACK (after lock)
┌──────────────────────────┐         ┌──────────────────────────┐
│ You owe Faizan            │         │ £51.40 of £74.93 back ▓▓░ │
│        £23.51             │         │ F  You    paid the bill   │
│ Ruby £15.90 · ½ Daal £4.95│         │ P  Priya   £16.82  ✅      │
│ service £2.66             │         │ T  Tom     £24.58  ⏳ [Mark]│
│ [ Pay on Monzo        ]   │         │ 🪫 Sam     £18.20  ⏳ [Mark]│
│ [ Revolut ] [Copy £23.51] │         │ [ Chase on WhatsApp 💬 ]  │
│ Bank 04-00-04 12345678 ⧉  │         └──────────────────────────┘
│ [ I've paid ✅ ]          │
└──────────────────────────┘          WHEEL: everyone's phone + big screen
                                      spin together → "🎉 Tom pays £74.93"
```

---

## 6. Data Model (Lovable Cloud / Postgres)
Claude runs this through the Lovable MCP `query_database` tool. **Measured: free, no credits used.** ✅ Checked on Lovable Cloud on 28 Oct (inside a transaction that was rolled back, so nothing was kept).

```sql
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
```
- **No storage bucket** (v3.1): photos go to the reader as base64 and are never kept.
- **Codes:** generated on the client from the 31-char alphabet. Retry on a unique-violation error.
- **Security note:** open RLS + a guessable code means anyone who guesses a code can read the table, **including the host's bank details at any time through the API** (the app only *shows* them after lock). That's accepted for a hackathon (C6 limits exposure). Real fix: longer codes for links + a short-lived join code. Lovable's security scan **will** flag the policies, which is expected.
- **Seed:** table `DEMO`, "Dishoom Kensington", 1 receipt (service included £8.33, total £74.93): Chicken Ruby 1590 · House Black Daal 990 · Lamb Biryani 1690 · Garlic Naan 450 · Garlic Naan 450 · Okra Fries 550 · Mango Lassi 550 · Masala Chai 390. **For testing only: it has no host, so never demo from it.**

---

## 7. The Maths (rules) → code in Appendix A
1. Everything is integer **pence**. Never floats, never VAT.
2. **Items mode:** an item claimed by *k* people splits into *k* parts that add up exactly. Service is shared in proportion to food, **per receipt**, then summed across rounds (`computeBill`). Service on unclaimed items stays unallocated.
3. **Even mode:** `computeEven(billTotal, everyone)`, penny-exact, host included.
4. **Wheel:** `computeWheel` (the winner owes `billTotal`; used when `wheel_pay_to = 'host'`). Slices in `wheelOrder` (by id). `pickWinner` uses `crypto.getRandomValues`. `wheelRotation(i, n)` lands slice *i* under the top pointer (tested for 2, 3, 5 and 8 players). Settled: pay to waiter → on spin; pay to host → when the winner pays, or straight away if the host won.
5. **Review check:** compare `receipt_total_pence` with **items + service** for that receipt, never items alone.
6. **No negative items.** Discounts are reported separately and applied by the host editing prices.
7. **Settled** = `isSettled()`: everything claimed, at least one non-host owes money, and all of them have paid. Never a bare `.every()`.
8. When everything is claimed: **sum of shares = sum of receipt totals, to the penny.**

---

## 8. Receipt Reading (Edge Function `parse-receipt`)
- **Client:** `<input type="file" accept="image/*" multiple>`, up to 4 photos per receipt. Resize each to ≤1600px JPEG on a canvas. **If a photo won't decode (e.g. HEIC in desktop Chrome), send the original.** Send them as base64 in the request body; never store them. Show "Reading receipt…" (5–15s).
- **Server:** **Lovable AI, the built-in gateway (`LOVABLE_API_KEY`, set by Lovable Cloud)**, with a vision-capable model: `google/gemini-2.5-flash`, or the current Gemini Flash if that's retired. Never ask the user for a key. Send **all photos of one receipt in one request**, with tool calling / a strict JSON schema:
```json
{
  "restaurant_name": "string",
  "items": [{ "name": "string", "quantity": 1, "line_total_pence": 450 }],
  "service_charge_pence": 833,
  "discount_pence": null,
  "receipt_total_pence": 7493
}
```
- **Instructions to the model:** *"These photos are parts of ONE receipt, in order, and may overlap. Return each line item exactly once: if a line appears in two photos, include it once."* Prices are integer pence and `line_total_pence` is the printed line price (for "2 x Burger @ 12.95  25.90" that's quantity 2 and 2590, never the @ unit price). Ignore subtotal, net and VAT summaries, payment/card lines, table numbers and covers. A printed service/"optional gratuity" line goes in `service_charge_pence`, never in items. Discounts go in `discount_pence` (positive), never in items.
- **After reading:** turn quantities into separate unit rows (spreading leftover pennies). `service_mode = 'included'` if service was found, otherwise `'add'` 12.5%. Always land on Review. If `discount_pence` is set, show *"Receipt has a £X discount: edit prices to apply it."*
- **Failure (>20s or error):** *"Couldn't read that one. Type it in or use the demo receipt."*
- AI calls use the same credit/usage balance. Read the demo receipt once in rehearsal and keep the result.

---

## 9. Lovable Build: Prompt Pack & Credits

### Credits (measured in the test run)
- **Prompt 1a (UI shell, 4 routes) cost 4.9 credits.** Lovable also wrote tests and ran browser checks, which add cost. **Budget ~5 credits per big prompt and ~1–2 per small fix.**
- **Free (measured or per MCP docs):** `query_database` (SQL), `enable_database`, `deploy_project`, project knowledge, reading files/diffs. Code pushed via **GitHub sync** should be free too (⏳ not yet tested).
- **Plan: P1–P5 ≈ 20–25 credits + spares. P6 (rounds) is cut for tonight.** **Update 28 Oct: hackathon credits are effectively unlimited**, so prefer Lovable prompts for every change. GitHub sync is optional (a nice-to-have for speed, not for cost). Time and the 20:45 freeze are the real limits now.
- **Every prompt ends with:** *"Don't write tests or run browser checks; we verify separately. Don't change files or behaviour not mentioned here."*
- **Order on the day:** `create_project` (P1) → `set_project_knowledge` (Prompt 0) → `enable_database` + §6 SQL + seed (free) → P2 → P3 → P4 → P5.

### Prompt 0: Project Knowledge (free; set right after `create_project`)
> TabSplit: a no-login web app for splitting a restaurant bill. Money is ALWAYS integer pence; never floats, never add VAT. Every money calculation uses `src/lib/split.ts` (computeSplit, computeBill, computeEven, computeWheel, allocate, isSettled, wheelOrder, pickWinner, wheelRotation, formatGBP, monzoLink); never reimplement or modify it. Routes are only `/`, `/new`, `/t/:code`, `/t/:code/screen`. Identity is the localStorage key `tabsplit:guest:<code>`; recent tables are the key `tabsplit:recent`. Share links are `window.location.origin + '/t/' + code`. `/t/:code/screen` must fit one screen with no scrolling. Phones need ≥72px bottom padding. Design: receipt-paper off-white, ink-black, monospace prices, one bold accent, green = claimed, pulsing red = unclaimed. No auth, no payment processing, no extra routes. Don't write tests or run browser checks.

### P1: UI Shell (sent as `create_project`'s `initial_message`)
> Build the UI for TabSplit, a mobile-first web app for splitting a restaurant bill. **UI only, no backend yet:** typed mock data in `src/lib/mock.ts` shaped exactly like these tables: [paste the §6 column lists for bills, receipts, items, guests, claims]. Create `src/lib/split.ts` with exactly this code and use it for every total: [paste Appendix A].
> Routes:
> - `/`: "Start a table", a "Join" box for a 4-character code, and "Your recent tables".
> - `/new`: 3 steps on one route. (1) Receipt: Use demo receipt (fills step 2 with the Dishoom items) / Type it in / Add photos (a placeholder for now). (2) Review: editable items, the check line "Receipt says £Y, we count £X (items + service)", and the service selector. (3) You: host name, Monzo, Revolut, sort code, account number (all optional) → "Open the table". Remember these on this phone (localStorage `tabsplit:host`) and pre-fill them next time. Strip a leading @, any monzo.me/ or revolut.me/ prefix and all spaces from the Monzo and Revolut fields.
> - `/t/:code`, with states switched by a dev toggle for now:
>   - Pick: item cards, tap to claim/unclaim, shared ÷ n, sticky "Your share" footer + Continue.
>   - Table: an "N unclaimed · £X" pill that expands, then you first, then everyone else with their items and totals, and "← Edit my items".
>   - Pay: "You owe Faizan £X", breakdown, Monzo/Revolut/Copy amount/Bank transfer with copy buttons, "I've paid".
>   - Track (host): rows with owes/paid, Mark paid/Undo, Chase on WhatsApp.
>   - Who are you?: unpaid non-host names, with "Just watching 👀" on top.
>   - Settled: ✅ + confetti.
>   - The host claims their own food like everyone else (same Pick ⇄ Table buttons), and also has a permanent host bar with **Lock bill**, Share, QR, Big screen and a ⚙️ menu (mode, add person, reset).
> - `/t/:code/screen`: a read-only projector view that fits 100vh, with a big QR of the table link and the code in huge type, and it follows the table's state. Claiming: items with claimer chips (unclaimed pulse red), people + totals, a "£X of £Y claimed" bar and the unclaimed pill. Locked: people with paid ✅ / owes ⏳ and a "£X of £Y back" bar. Settled: a big Settled ✅.
> Guests get a random funny food alias + emoji with inline rename, and no name gate. Design: [Prompt 0 design line]. The attached images are layout references for Pick, Table, Pay, Track and the big screen (1280×720). Ignore the "Who had the …?" banner in the Pick image (it comes later). Where an image and this text differ, this text wins. Don't write tests or run browser checks.

### (free) Claude: `enable_database` → §6 SQL → seed `DEMO` → verify with a `select`.

### P2: Wire Data + Realtime + Lock/Pay (Phase A complete)
> The tables bills, receipts, items, guests and claims already exist with seed table `DEMO` (created outside Lovable). Don't create or alter tables or run migrations. If `src/integrations/supabase/types.ts` doesn't include them, regenerate it from the live database; if you can't, type the queries with the row types in `src/lib/mock.ts` through one small helper. Replace all mock data with real queries, and remove the dev toggle: the screen follows the bill's status and your role (claiming → Pick ⇄ Table; locked → Pay for guests, Track for the host; settled → Settled).
> `/new` creates a bill (random 4-char code from ABCDEFGHJKMNPQRSTUVWXYZ23456789, retry if taken), one receipt, its items and a host guest (is_host=true), saves the host's id in `tabsplit:guest:<code>`, adds the code to `tabsplit:recent`, and goes to `/t/:code`.
> On `/t/:code` (never on `/screen`), in a client-only effect after the bill and guests load: if `tabsplit:guest:<code>` is missing (or not in the guest list) and the bill is claiming, **generate the id with `crypto.randomUUID()`, save it to localStorage BEFORE the request, then upsert the guest row with that id** and the alias, so a double effect or re-render can never create two guests. Never read localStorage during server render. If the bill is locked and there's no local identity, show "Who are you?" listing only unpaid non-host guests, with "Just watching 👀" (view only, no guest row) on top. Taps insert/delete claims optimistically.
> Realtime on `/t/:code` and `/screen`: subscribe to postgres_changes with **`id=eq.<bill.id>` for bills** and **`bill_id=eq.<bill.id>` for receipts, items, guests and claims**. On any event, debounce a refetch by 250ms, ignore stale responses, and keep taps that are still saving on top. Also refetch on reconnect and on `visibilitychange`.
> Host actions:
> - Lock: a permanent footer button; status=locked; it pulses when 0 items are unclaimed. Before inserting a claim, check the bill is still claiming; if not, undo the tap and show "The bill's locked".
> - Reset: delete claims; clear paid_at, wheel_winner_id, wheel_spun_at and settled_at; status=claiming.
> - Mark paid / Undo: set or clear paid_at.
> Guest "I've paid" sets paid_at. When `isSettled()` becomes true, set status=settled + settled_at. Pay methods are shown only if the host filled them in. Bank details are shown only after lock.
> Share button: `navigator.share` with "Join our table on TabSplit: <link> (code <code>)", falling back to copying the link. Don't write tests or run browser checks.

### P3: Receipt Photos (Phase B)
> On `/new` step 1, "Add photos" accepts up to 4 images for one receipt (`accept="image/*" multiple`). Resize each to max 1600px JPEG; if one can't be decoded, send the original. Send each as a full `data:image/jpeg;base64,…` data URL in the request body. **Don't create a storage bucket or store photos.**
> Add "Tonight's receipt": in rehearsal the host picks up to 4 photos once; keep them resized (max 1280px) in localStorage under `tabsplit:tonight`, and one tap sends them to the reader without opening the picker. A small "Change saved photos" link replaces them.
> Create the edge function `parse-receipt`, called with `supabase.functions.invoke`; it must work without login (`verify_jwt = false`). It uses **Lovable AI, the built-in gateway with `LOVABLE_API_KEY`. Do not ask me for any API key.** Use the vision-capable model `google/gemini-2.5-flash` (or the current Gemini Flash if that's retired), send all photos in one request as `image_url` parts with the data URLs, and use tool calling that returns exactly: [paste §8 schema + instructions].
> Turn quantities into unit rows (spread leftover pennies), never create negative items, set `service_mode = 'included'` with `service_included_pence = service_charge_pence` only if `service_charge_pence` is above 0 (null or 0 → `'add'` at 12.5%), show "Receipt has a £X discount: edit prices to apply it." if `discount_pence` is above 0, and land on Review. Show "Reading receipt…". On error or after 20s, show "Couldn't read that one. Type it in or use the demo receipt." Don't change other screens. Don't write tests or run browser checks.

### P4: Modes + People (Phase C)
> Add a host ⚙️ mode switch: Split by items / Split evenly / Spin for it 🎡. While claiming it switches freely; when locked or settled it asks to confirm, then sets status=claiming and clears paid_at, wheel_winner_id, wheel_spun_at and settled_at.
> **Even:** skip Pick: guests go straight to the Table view with a "£X each × N" banner instead of the unclaimed pill. Totals come from `computeEven(billTotal, all guest ids including no-phone people)`, and after lock Pay, Track, `/screen` and `isSettled()` use that same result. `/screen` shows the equal shares.
> **Wheel:**
> - Everyone is on the wheel by default (`guests.in_wheel` defaults to true). Each phone shows a big "Sit this one out" toggle. The host can sit out people without a phone.
> - With ≥2 in, the host taps Spin: `pickWinner(wheelOrder(in-wheel ids))`, then save `wheel_winner_id` and `wheel_spun_at = now()`.
> - Slices: equal, starting at the top, clockwise, in `wheelOrder` (by guest id, never by name). On every phone and on `/screen`, **start the 5s spin (0 → `wheelRotation(winnerIndex, n)` degrees, ease-out) when `wheel_winner_id` changes from null to a value while the page is open.** Don't time the animation from `wheel_spun_at`, because phone clocks drift. If the page *loads* with a winner already set, show the result without spinning.
> - While mode is wheel, every phone and `/screen` keep the wheel on screen whatever the status (a settled status must never replace it before the spin ends). After the 5s spin, show the result card under the wheel.
> - Result: "🎉 <name> pays £<billTotal>", with totals from `computeWheel`. The host chooses `wheel_pay_to`: waiter → status=settled; host → the winner sees the Pay screen for the full amount, and the bill is settled when they mark paid (or straight away if the host won).
> **Add person without a phone (host):** "+ Add person" creates a guest with has_phone=false and a 🪫 emoji. They count in Split evenly and the wheel only; hide them in Split by items. The host can mark them paid.
> Show a "Who had the <item>? 👀" banner when 1–2 items remain unclaimed. Don't write tests or run browser checks.

### P5: Polish + Demo Safety
> - The Track screen gets "Chase on WhatsApp": `https://wa.me/?text=` with "Still owed for <restaurant> 🧾 <name> £x · <name> £y, pay here: <link>".
> - Confetti (canvas-confetti) on Settled and on the wheel result.
> - `/t/:code?demo=1` shows "Simulate table", which adds 4 guests (Priya, Tom, Sam, Jess) who claim random unclaimed items 1–2s apart.
> - Make sure `/t/:code/screen` never scrolls at 1280×720 and 1920×1080, and that phones have ≥72px bottom padding.
> Don't write tests or run browser checks.

### P6: Rounds (Phase D) ✂️ cut for tonight, kept for later
> The host ⚙️ gets "Add another round": runs `/new` steps 1–2 for a new receipt on the same bill. Items are grouped by round label on Pick, Table and Screen. All totals use `computeBill(receipts with their items and service, claims, guestIds)`. Don't write tests or run browser checks.

**Rule:** never spend credits arguing with a broken layout. **Roll back** to the last good version (free) and reword.

---

## 10. Workflow: Claude + Argon + Lovable
| Who | Role |
|---|---|
| **Claude** (lead) | Spec, prompts, SQL, maths, reviews every Lovable change (`read_file`/`get_diff`), checks the DB, makes small fixes through GitHub when connected |
| **Argon** 🔍 | Critic at fixed checkpoints: spec review (now), demo red-team (20:30), Q&A grilling (21:15) |
| **Lovable** | Builds the UI, hosts, Cloud DB, Lovable AI |
| **Faizan + team** | Product decisions, phones, testing, pitch |

Golden rules: one big prompt per phase · roll back instead of arguing · **feature freeze 20:45** · Claude pulls before every push.

---

## 11. Test Run Results & Checklist

### Results (28 Oct, morning; project "TabSplit: Shared Plates", `tabsplit-test.lovable.app`)
- ✅ Lovable MCP works from a **cloud** Claude session.
- ✅ The UI shell (4 routes, design, QR, aliases, rename, local claiming) came out in one prompt. **4.9 credits.**
- ✅ The stack is **TanStack Start** (file routes like `src/routes/t.$code.tsx`). Lovable handles it.
- ✅ The guest phone screen works on an iPhone (claiming Okra Fries → share £6.19).
- ⚠️ The **table screen overflowed** a laptop window (bottom rows cut off). P1/P5 now require `/screen` to fit 100vh.
- ⚠️ The **"Edit with Lovable" badge** covered the share footer on the phone. ≥72px bottom padding is now required.
- ⚠️ Strict TypeScript rejected the original `split.ts`. Fixed: Appendix A passes `--strict --noUncheckedIndexedAccess`.
- ✅ The database setup via `query_database` and publishing were **free**.
- ℹ️ Free plan = **5 credits/day** (resets 00:00 London). Today's are used up, so further testing has to be free (SQL, GitHub) until the event.

### Still to check (free, before 18:00)
- [ ] GitHub sync: connect the repo in Lovable, Claude pushes a fix, and it appears in Lovable with no credits spent.
- [ ] `monzo.me/<user>/1.50?d=test` opens Monzo with £1.50 filled in, and what a non-Monzo phone sees.
- [ ] What `revolut.me/<tag>` does on a phone.
- [x] 3 test receipts (one long, one with service printed, one with 2× items): **AI-generated with Gemini 4 Argon (Faizan's call)**, text checked line by line, in `assets/receipts/` with the expected reader output in `EXPECTED.md`. Plus a backup stage receipt `assets/demo-receipt.png` (= the DEMO seed). On stage, tonight's real receipt is still the best one.
- [x] Continue the test project or start fresh? **Fresh.** The morning project was a personal test, not an event entry. Paste-ready prompts + SQL are in `build/` (see `build/README.md`); the test project's look is pinned into P1.
- [x] Screen mockups (Pick, Table, Pay, Track, wheel): `mockups/all-screens.png`, amounts computed with `split.ts`.

---

## 12. Hackathon Timetable (today, 18:00 – 22:00)
**Before 18:00:** this doc final + Argon-reviewed, prompts ready, Monzo username + bank details ready, receipt photos taken, phones charged, a hotspot, credits confirmed.

| Time | What | Credits |
|---|---|---|
| 18:00–18:15 | P1 (`create_project`) · Prompt 0 · DB + seed (free) | ~5 |
| 18:15–19:00 | P2 → **2 phones: join by code, claim, lock, pay, ✅ by 19:00** | ~5 |
| 19:00–19:35 | P3 receipt photos → test with tonight's receipt | ~4 |
| 19:35–20:10 | P4 modes + wheel + no-phone person → wheel on 3 phones | ~5 |
| 20:10–20:35 | P5 polish → publish | ~3 |
| 20:35–20:45 | 🔍 Argon red-team of the live app · last small fixes | 0–2 |
| **20:45** | **🔒 Feature freeze** | |
| 20:45–21:15 | 5 phones, venue Wi-Fi + 4G, full loop ×3 · **record a backup video** | 0 |
| 21:15–22:00 | 🔍 Argon Q&A grilling · rehearse ×3 · reset the demo table | 0 |

---

## 13. Demo & Stage Script (2 minutes; ending decided on the night)
**[0:00–0:20] Hook:** *"Hands up if you've been at a group dinner and when the bill arrived, everyone went quiet?"* … *"and one person puts their card down and spends a week chasing friends on Monzo."*

**[0:20–0:55] Join + claim:** hold up tonight's receipt → tap **Tonight's receipt** → items appear (fallback: **Use demo receipt**). *"Normally I'd drop the link in our group chat. Tonight you're my dinner party: scan the screen and tap what you ate."* Aliases pop up on the big screen. *"Shared the pizza? Tap it too, and it splits, service and all, to the penny."*

**[0:55–1:20] The money:** point at the pill: *"3 things nobody's claimed: who had the garlic bread? 👀"* Lock. *"Now your phone says exactly what you owe me, and one tap opens Monzo with the amount filled in."* A teammate pays → ✅ on screen.

**[1:20–1:45] The wheel (if we pick the wheel ending at 21:15):** *"Of course, some tables don't split. They spin."* Switch to 🎡 (everyone who scanned is already on it) → *"Sit out now if you can't afford Dishoom."* → **every phone in the room spins at once** → *"🎉 …pays the waiter £74.93"* → **Settled ✅ + confetti**.

**[1:45–2:00] Close:** *"Splitwise launched receipt splitting two weeks ago, so the problem is real. But it ends with an IOU. TabSplit ends with the host paid before the waiter's back. TabSplit: get paid before anyone stands up."*

**If we pick the confetti ending instead:** judges won't really pay, so the host marks them paid as cash and *says so*.

**Fallbacks:** few scans → teammates' phones + Simulate table (say so). Wi-Fi dead → backup video. Phone not allowed on the projector → MacBook iPhone Mirroring or `/screen` on the laptop.

---

## 14. Q&A Prep
* **"Doesn't Splitwise do this now?"** *"Since 14 October, yes, which validates the problem. Splitwise is a ledger: the result is a balance you settle later. We're built for the 5 minutes at the table, with UK bank links filled in, a bill that isn't done until the host is paid, and modes like the wheel that make it fun."*
* **"How do you make money?"** *"Consumer-first today: every table reaches ~6 people for free. The money is in guests paying the venue directly by bank from this screen, through a licensed pay-by-bank provider. The venue saves on card fees and turns tables faster, and we take a cut of the saving."*
* **"Why won't Monzo or Splitwise copy this?"** *"They might. Monzo only works if the whole table banks with Monzo. We're bank-neutral. Splitwise is a ledger you keep coming back to. We're built for the five minutes at the table. Speed and focus, and we'd measure whether groups come back."*
* **"How do you know someone actually paid?"** *"Today it's honour system plus the host as referee: they can undo a tick or mark cash. Automatic confirmation through Open Banking is the next step, and it's also the business model."*
* **"Isn't the wheel gambling?"** *"It's the card roulette friends already play, made fair and visible. It's opt-in, between friends, and no money comes to us or anyone outside the table."* (Don't make legal claims beyond that.)
* **"A 4-character code can be guessed. Can strangers see my bank details?"** *"Honestly, tonight that's a UI gate: the app only shows them after the host locks. The real product replaces raw bank details with pay-by-bank links, so there's nothing to leak, plus longer private links and tables that delete themselves."*
* **"What if the AI misreads the receipt?"** *"The host reviews it first, with a check against the printed total, so a misread is fixed in two taps."*
* **"What if someone claims the wrong thing?"** *"Tap again to unclaim. Everyone sees the whole table, so mistakes get noticed before the host locks."*

---

## 15. Argon Review, Round 1 (v2.1): What We Took and What We Didn't
> Historical. Some fixes were superseded in v3: the host now creates and claims on their own phone (so the `?g=` host QR is gone), and routes are `/t/:code` + `/t/:code/screen`.
Argon's verdict: **build with fixes.** Claude checked each finding.

| Argon finding | Decision | What changed |
|---|---|---|
| Live camera + HEIC + 6–12s parse will stall on stage | ✅ Accepted, adjusted | "Tonight's receipt" preset parsed live with one tap, no camera picker. Fallback to the original file if canvas decode fails. Timeout 20s. *Note: iOS Safari usually converts HEIC→JPEG on upload, so the real risk is a Mac/Chrome upload.* |
| Name entry kills the 5-second scan moment | ✅ Accepted | Instant food alias + optional rename. Guest row created on first tap *(superseded in v3.1: created when the page opens)*. |
| Refetch storm overwrites optimistic taps | ⚖️ Partly | Kept refetch (simpler, can't drift out of sync), but **debounced, latest wins, taps still saving stay on top**, plus refetch on reconnect/wake. Patching state from realtime payloads is more code for Lovable to get wrong. |
| `.every()` confetti fires on an empty table | ✅ Accepted, a real bug | `isSettled()` added to `split.ts` and tested. |
| Review check compares items to a receipt total that includes service | ✅ Accepted, a real bug | Compare items + service. |
| Negative discount items break claiming and the maths | ✅ Accepted, a real contradiction | `discount_pence` field, never claimable rows. |
| `bills` has no `bill_id`, so the realtime filter breaks | ✅ Accepted, a real bug | `id=eq.` for bills, `bill_id=eq.` for the rest. |
| Prompt 1 too dense | ✅ Accepted | Split into 1a (UI shell) → Claude runs SQL (free) → 1b (data + realtime). Review folded into `/new`. |
| Hardcode gateway URL + `gemini-2.5-flash` | ⚖️ Partly | Prompt names Lovable AI + `LOVABLE_API_KEY` and forbids asking for a key, but **doesn't pin a model**. A hardcoded model name may be outdated by now, and Lovable picks its own current default. |
| Host can't claim their own food | ✅ Accepted, a real gap | "Claim as host" QR (`?g=`). |
| Cut Revolut | ❌ Kept | It's one button. Half of a London table uses Revolut. With no pre-filled amount, it sits next to "Copy amount". |
| "Venues pay for the settled screen" won't convince seed VCs | ✅ Accepted, different fix | Lead with **guests paying the venue by bank (pay-by-bank)**. Rejected Argon's "PISP micro-fee on friend payments": people won't pay a fee to pay a friend. |
| Unprepped "Why won't Monzo/Splitwise copy this?" | ✅ Accepted, answer rewritten | Rejected Argon's claim that it "cannibalises Splitwise's install funnel" as speculation we can't back up on stage. |
| One big idea: zero-typing join + WhatsApp "Receipt of Shame" image | ✅ Join accepted · ⚖️ share as **text** | `wa.me` text link instead of an image card: same laugh, 1/10th of the build. |


---

## 16. Argon Review, Round 2 (v3.1): What We Took and What We Didn't
Argon's verdict: **build with fixes.** Claude checked each finding.

| Argon finding | Decision | What changed |
|---|---|---|
| Storage bucket in P3 is a 30-min trap (storage RLS), and photos are never shown again | ✅ Accepted | No bucket, no `photo_paths`. Photos go to the reader as base64. "Tonight's receipt" photos are kept on the host's phone (localStorage). |
| Claiming for a no-phone person tangles identity state | ✅ Accepted | No-phone people count in Split evenly + the wheel only. In items mode a friend claims for them. |
| `receipts` adds complexity before it's needed | ⚖️ Partly | Rounds (P6) are cut for tonight. **Kept the `receipts` table** with one row per table: it holds the service settings, the SQL is already tested, and `computeBill` handles it. That's no extra work for Phase A. |
| Guest row created on first tap breaks the "aliases pop up" moment, rename, even and wheel | ✅ Accepted, **a real bug in v3** (Claude's own change from round 1) | Guest row created when the page opens (claiming only, never on `/screen`). Joiners who eat nothing show £0 and can be removed. |
| Late scanners after lock hit "Who are you?" and grab someone's identity | ✅ Accepted | Only unpaid non-host names, plus "Just watching 👀". |
| Lock buried in ⚙️ | ✅ Accepted | Permanent Lock button in the host's footer. Taps arriving after lock are undone. |
| `in_wheel` default false leaves the Spin button dead on stage | ✅ Accepted, **with consent kept** | Opt-out: everyone is on the wheel, with a big "Sit this one out" button. |
| Clock drift skips the wheel animation | ✅ Accepted, **a real bug in v3** | Spin starts when a phone *sees* the winner appear (realtime), not from `wheel_spun_at`. On page load with a winner already set, show the result. |
| Slices by name break on rename; `isSettled` fails for the wheel | ✅ Accepted | `wheelOrder` (by id) + `computeWheel` added to `split.ts` and tested. Wheel settle rules written out (host-wins case included). |
| Seed `DEMO` has no host | ✅ Accepted | "Use demo receipt" fills Review and the host creates a real table. Never demo from `/t/DEMO`. |
| Pin `google/gemini-2.5-flash` in P3 | ⚖️ Partly (changed from round 1) | Named as the model **with a fallback** "or the current Gemini Flash if that's retired". Argon raised it twice, and naming it is cheap if worded safely. |
| C6 isn't DB-level security | ✅ Accepted | C6 and the §14 answer now say "UI gate tonight; pay-by-bank links are the real fix". |
| Q7: A → B (base64) → C → cut D | ✅ Agreed | Recorded in §0. |
| Q8: end on the wheel after a pay ✅ | 📝 Noted | Faizan decides on the night. Claude added: a real "everyone paid" Settled can't happen with judges, so the wheel is the natural way to show Settled. |

---

## 17. Argon Review, Round 3 (v3.2): the Build Kit + Mockups (28 Oct, 16:45)
Argon 4 (High) via `agy -p`, read-only, over `build/`, the mockups and `EXPECTED.md`. Raw output: `reviews/argon-build-kit-raw.txt`. Claude checked each finding.

| Argon finding | Decision | What changed |
|---|---|---|
| The wheel view can be replaced by Settled at once (status=settled on spin), so the 5s spin never plays; Reset and the mode switch never clear `wheel_winner_id`, so a rehearsed table can't spin again | ✅ Accepted, **two real bugs** | P4: the wheel stays on screen in wheel mode whatever the status, result card after the spin. Reset (P2) and the mode switch (P4) clear `wheel_winner_id`, `wheel_spun_at`, `settled_at` |
| Guest row created by an async effect: a StrictMode double effect or a re-render inserts **two guests per phone**; localStorage read during server render | ✅ Accepted, a real bug | P2: client-only effect, `crypto.randomUUID()` saved to localStorage *before* the request, then upsert with that id |
| `/screen` only specified for claiming, but the pitch says "a teammate pays → ✅ on screen" | ✅ Accepted, a real gap | P1: `/screen` follows the state (claiming / locked with paid ✅ owes ⏳ and "£X of £Y back" / settled). P4: even shares on `/screen` |
| Host retypes 5 payment fields on stage; "@user" or a pasted monzo.me link breaks the pay link | ✅ Accepted | P1 step 3: remembered in `tabsplit:host` and pre-filled; @, monzo.me/, revolut.me/ and spaces stripped |
| Mockups: notes inside the phones get copied into the UI; attaching the wheel to P1 invites an early wheel; host's claiming footer unclear; "Who had the…" banner is a P4 feature | ✅ Accepted | Notes removed from the phone images. P1 attaches 5 images (wheel goes with P4). The host claims with the same Pick ⇄ Table buttons plus a host bar (Lock bill, Share, QR, Big screen, ⚙️). P1 says to ignore the banner |
| P3: `service_charge_pence: 0` read as "service found" (fails `crown-anchor`); raw base64 instead of data URLs → gateway 400; anon calls 401 without `verify_jwt = false`; "Tonight's receipt" can't be replaced | ✅ Accepted · ⚖️ one part | Service/discount only count when above 0; full `data:image/jpeg;base64` URLs as `image_url` parts; `supabase.functions.invoke` + `verify_jwt = false`; "Change saved photos" link. **Not taken:** hardcoding the gateway URL (Lovable knows its own gateway; same call as round 1) |
| Tables made with `query_database` may leave `types.ts` empty, so strict TS fails in P2 | ⚖️ Partly | P2 asks Lovable to regenerate `types.ts` from the live DB first, with a typed helper over `mock.ts` rows as the fallback (not Argon's `supabase as any`) |
| `guests.color` is NOT NULL with no default, so "+ Add person" and "Simulate table" inserts fail | ✅ Accepted, a real bug | `color ... default 'oklch(0.52 0.22 262)'` |
| Even mode underspecified: guests stuck on Pick, Pay/Track fall back to item totals | ✅ Accepted | P4: even mode skips Pick, Table shows "£X each × N", and Pay/Track/`/screen`/`isSettled()` all use `computeEven` |
| Run order: `enable_database` while P1 may still be running; `wheel.png` uploaded at 18:00 expires before P4; nothing published before 20:10, so phones can't test | ✅ Accepted | `build/README.md`: wait for P1 to finish, upload the wheel at P4, `deploy_project` (free) after every phase |

---

## Appendix A: `src/lib/split.ts` (tested 28 Oct 2026, passes `tsc --strict --noUncheckedIndexedAccess`)
Covered by 20 tests: shared items · unclaimed items · exact totals with 12.5% added · service already on the receipt · empty bill · Monzo link format · `isSettled` (empty table, unclaimed item, unpaid guest, host doesn't need to pay) · **two rounds with different service rules add up exactly (£83.66)** · **even split £74.93 ÷ 3 is penny-exact** · **winner is always a player** · **wheel lands on the winner's slice for 2, 3, 5 and 8 players** · **wheel: winner owes the bill, settled once they pay, host-wins handled by the prompt rule** · **wheel order is by id, not name.**

```ts
// All money is integer pence. Never use floats for money.
export type Item = { id: string; price_pence: number };
export type Claim = { item_id: string; guest_id: string };
export type ServiceMode = "none" | "add" | "included";
export type Service = { mode: ServiceMode; rate: number; included_pence?: number };

// Split `total` across weights so the parts always sum to exactly `total` (largest remainder).
export function allocate(total: number, weights: Record<string, number>): Record<string, number> {
  const ids = Object.keys(weights).sort();
  const sum = ids.reduce((s, id) => s + (weights[id] ?? 0), 0);
  const out: Record<string, number> = {};
  if (sum <= 0 || total === 0) { ids.forEach((id) => (out[id] = 0)); return out; }
  const raw = ids.map((id) => ({ id, exact: (total * (weights[id] ?? 0)) / sum }));
  raw.forEach((r) => (out[r.id] = Math.floor(r.exact)));
  let left = total - raw.reduce((s, r) => s + (out[r.id] ?? 0), 0);
  raw.sort((a, b) => (b.exact - Math.floor(b.exact)) - (a.exact - Math.floor(a.exact)) || a.id.localeCompare(b.id));
  for (const r of raw) { if (left <= 0) break; out[r.id] = (out[r.id] ?? 0) + 1; left -= 1; }
  return out;
}

export function computeSplit(items: Item[], claims: Claim[], guestIds: string[], service: Service) {
  const food: Record<string, number> = Object.fromEntries(guestIds.map((g) => [g, 0]));
  const unclaimed: Item[] = [];
  for (const item of items) {
    const claimers = [...new Set(claims.filter((c) => c.item_id === item.id).map((c) => c.guest_id))]
      .filter((g) => g in food);
    if (claimers.length === 0) { unclaimed.push(item); continue; }
    const parts = allocate(item.price_pence, Object.fromEntries(claimers.map((g) => [g, 1])));
    for (const g of claimers) food[g] = (food[g] ?? 0) + (parts[g] ?? 0);
  }
  const itemsTotal = items.reduce((s, i) => s + i.price_pence, 0);
  const serviceTotal =
    service.mode === "add" ? Math.round(itemsTotal * service.rate)
    : service.mode === "included" ? (service.included_pence ?? 0)
    : 0;
  const claimedFood = Object.values(food).reduce((s, v) => s + v, 0);
  // Service on unclaimed food stays unallocated until those items are claimed.
  const serviceForClaimed = itemsTotal === 0 ? 0 : Math.round((serviceTotal * claimedFood) / itemsTotal);
  const svc = allocate(serviceForClaimed, food);
  const perGuest = guestIds.map((g) => ({
    guest_id: g, food_pence: food[g] ?? 0, service_pence: svc[g] ?? 0, total_pence: (food[g] ?? 0) + (svc[g] ?? 0),
  }));
  const billTotal = itemsTotal + serviceTotal;
  const claimedTotal = perGuest.reduce((s, p) => s + p.total_pence, 0);
  return { perGuest, unclaimed, billTotal, claimedTotal, remaining: billTotal - claimedTotal };
}

export const formatGBP = (p: number) => `£${(p / 100).toFixed(2)}`;
// TODO verify in test run: monzo.me/<username>/<amount>?d=<description>
export const monzoLink = (user: string, pence: number, note: string) =>
  `https://monzo.me/${encodeURIComponent(user)}/${(pence / 100).toFixed(2)}?d=${encodeURIComponent(note)}`;

export type Guest = { id: string; is_host: boolean; paid_at: string | null };
export type SplitResult = {
  perGuest: { guest_id: string; food_pence: number; service_pence: number; total_pence: number }[];
  unclaimed: Item[]; billTotal: number; claimedTotal: number; remaining: number;
};

// A table can have several receipts ("rounds"), each with its own service charge. Split each, then add up.
export type Receipt = { id: string; items: Item[]; service: Service };
export function computeBill(receipts: Receipt[], claims: Claim[], guestIds: string[]): SplitResult {
  const perGuest = guestIds.map((g) => ({ guest_id: g, food_pence: 0, service_pence: 0, total_pence: 0 }));
  const out: SplitResult = { perGuest, unclaimed: [], billTotal: 0, claimedTotal: 0, remaining: 0 };
  for (const r of receipts) {
    const s = computeSplit(r.items, claims, guestIds, r.service);
    s.perGuest.forEach((p, i) => {
      const t = perGuest[i];
      if (!t) return;
      t.food_pence += p.food_pence; t.service_pence += p.service_pence; t.total_pence += p.total_pence;
    });
    out.unclaimed.push(...s.unclaimed);
    out.billTotal += s.billTotal;
    out.claimedTotal += s.claimedTotal;
  }
  out.remaining = out.billTotal - out.claimedTotal;
  return out;
}

// "Split evenly" mode: everyone at the table (host included) gets an equal, penny-exact share of the whole bill.
export function computeEven(billTotal: number, guestIds: string[]): SplitResult {
  const parts = allocate(billTotal, Object.fromEntries(guestIds.map((g) => [g, 1])));
  const perGuest = guestIds.map((g) => ({ guest_id: g, food_pence: parts[g] ?? 0, service_pence: 0, total_pence: parts[g] ?? 0 }));
  return { perGuest, unclaimed: [], billTotal, claimedTotal: billTotal, remaining: 0 };
}

// Wheel mode: the winner owes the whole bill, everyone else owes nothing.
// Settled rules for the wheel (no claiming involved): pay_to 'waiter' → settled on spin;
// pay_to 'host' → settled when the winner marks paid, or straight away if the host won.
export function computeWheel(billTotal: number, winnerId: string, guestIds: string[]): SplitResult {
  const perGuest = guestIds.map((g) => {
    const t = g === winnerId ? billTotal : 0;
    return { guest_id: g, food_pence: t, service_pence: 0, total_pence: t };
  });
  return { perGuest, unclaimed: [], billTotal, claimedTotal: billTotal, remaining: 0 };
}

// Wheel slices are ALWAYS in this order (by guest id, never by name, so a rename can't move them).
export const wheelOrder = (guestIds: string[]): string[] => [...guestIds].sort((a, b) => a.localeCompare(b));

// Wheel: the host's phone picks the winner once and saves it; every phone animates to the same result.
export function pickWinner(guestIds: string[]): string {
  const r = new Uint32Array(1);
  crypto.getRandomValues(r);
  return guestIds[(r[0] ?? 0) % guestIds.length] ?? "";
}
// Clockwise rotation (degrees) that leaves the winner's slice under a pointer at the top (0°).
// Slice i covers [i*360/n, (i+1)*360/n) measured clockwise from the top before rotating.
export function wheelRotation(winnerIndex: number, n: number, turns = 6): number {
  const slice = 360 / n;
  return turns * 360 + (360 - (winnerIndex + 0.5) * slice);
}

// "Settled" only when every item is claimed, someone besides the host owes money, and all of them have paid.
export function isSettled(split: SplitResult, guests: Guest[]): boolean {
  const owing = split.perGuest.filter((p) => p.total_pence > 0 && !guests.find((g) => g.id === p.guest_id)?.is_host);
  return split.unclaimed.length === 0 && owing.length > 0
    && owing.every((p) => Boolean(guests.find((g) => g.id === p.guest_id)?.paid_at));
}
```

---

## Sources
- Splitwise Itemize launch (14 Oct 2026, free in US & UK, QR claiming without the app): [The Paypers](https://thepaypers.com/payments/news/splitwise-launches-itemize-receipt-splitting-feature-in-the-us-and-uk), [Yahoo Finance](https://finance.yahoo.com/small-business/articles/splitwise-launches-feature-takes-awkwardness-123000659.html), [Digital Trends](https://www.digitaltrends.com/phones/splitwise-now-lets-you-calculate-everyones-share-of-a-restaurant-bill-including-tax-and-tip/)
- No-download web splitters: [BillMath](https://www.billmath.com/), [BillTap](https://billtap.app/), [Divvi](https://justdivvi.com/), [SplitterUp](https://splitterup.app/blog/best-receipt-scanning-apps)
- Lovable MCP server (tools; only `create_project` / `send_message` use credits): [lovablelabs/mcp](https://github.com/lovablelabs/mcp), [Lovable docs](https://docs.lovable.dev/integrations/lovable-mcp-server)
- revolut.me links (no documented amount pre-fill): [Revolut help](https://help.revolut.com/en-JP/help/transfers/payment-links/revolut-me-link/)
- Lovable credit pricing (secondary sources, check against lovable.dev): [eesel.ai](https://eesel.ai/blog/lovable-pricing), [UsagePricing](https://www.usagepricing.com/blueprint/activity/lovable-2026-10-05-chat-pricing-daily-allowance)
