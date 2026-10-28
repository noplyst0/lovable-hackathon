-- Seed table DEMO (testing only: it has no host, so never demo from /t/DEMO)
with b as (
  insert into bills (code, restaurant_name) values ('DEMO', 'Dishoom Kensington') returning id
), r as (
  insert into receipts (bill_id, service_mode, service_included_pence, receipt_total_pence)
  select id, 'included', 833, 7493 from b returning id, bill_id
)
insert into items (bill_id, receipt_id, name, price_pence, position)
select r.bill_id, r.id, v.name, v.price, v.pos from r, (values
  ('Chicken Ruby', 1590, 1), ('House Black Daal', 990, 2), ('Lamb Biryani', 1690, 3),
  ('Garlic Naan', 450, 4), ('Garlic Naan', 450, 5), ('Okra Fries', 550, 6),
  ('Mango Lassi', 550, 7), ('Masala Chai', 390, 8)) as v(name, price, pos);

-- Verify: expect 8 items, 6660 pence of food, receipt total 7493
select b.code, count(i.*) as items, sum(i.price_pence) as food_pence, max(r.receipt_total_pence) as receipt_total
from bills b join receipts r on r.bill_id = b.id join items i on i.receipt_id = r.id
where b.code = 'DEMO' group by b.code;
