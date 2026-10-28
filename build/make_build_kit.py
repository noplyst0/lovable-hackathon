"""Regenerate the paste-ready build kit from TABSPLIT_IDEA2.md (the single source of truth).

Run from the repo root:  python3 build/make_build_kit.py
Code blocks (SQL, split.ts, the reader schema) are copied out of the spec verbatim, so a spec edit
followed by a re-run keeps every prompt in sync. Never hand-edit the generated .txt/.sql files.
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SPEC = (ROOT / "TABSPLIT_IDEA2.md").read_text()
OUT = ROOT / "build"


def section(start, end):
    i = SPEC.index(start)
    return SPEC[i:SPEC.index(end, i + len(start))]


def code_block(text, lang):
    m = re.search(r"```" + lang + r"\n(.*?)```", text, re.S)
    return m.group(1).rstrip() + "\n"


def quote(text, heading):
    """The '> ...' prompt paragraph that follows a ### heading, without the '> ' markers."""
    body = text[text.index(heading) + len(heading):]
    lines = []
    for line in body.splitlines()[1:]:
        if line.startswith(">"):
            lines.append(line[1:].lstrip(" ") if line.startswith("> ") else line[1:])
        elif lines:
            break
    return "\n".join(lines).replace("**", "").strip() + "\n"


schema_sql = code_block(section("## 6. Data Model", "## 7."), "sql")
split_ts = code_block(section("## Appendix A", "## Sources"), "ts")
reader_json = code_block(section("## 8. Receipt Reading", "## 9."), "json")
reader_rules = re.search(r"- \*\*Instructions to the model:\*\* (.*)\n", SPEC).group(1).replace("*", "")
prompts = section("### Prompt 0", "**Rule:**")

DESIGN = (
    "Design: receipt-paper off-white, ink-black text, monospace prices, one bold accent, green = claimed, "
    "pulsing red = unclaimed. Big tap targets. Mobile-first everywhere except /t/:code/screen, which is "
    "projector-first, must fit exactly 100vh and must never scroll. Every phone screen has at least 72px of "
    "bottom padding so the 'Edit with Lovable' badge never covers the sticky footer. Don't imitate Monzo or "
    "Revolut branding. Use exactly these tokens (they come from a version we liked): fonts Archivo (body), "
    "Archivo Black (headings), JetBrains Mono (prices and codes); colours in oklch: background 0.965 0.012 85, "
    "paper/cards 0.985 0.008 85, ink 0.17 0.01 60, the one accent is electric cobalt 0.52 0.22 262, "
    "claimed green 0.6 0.16 150, unclaimed red 0.58 0.22 27 (pulsing), warning amber 0.75 0.16 70. "
    "Receipt-style cards with a dashed rule between sections."
)

COLUMNS = """\
- bills: id uuid, code text (4 chars from ABCDEFGHJKMNPQRSTUVWXYZ23456789), restaurant_name text, mode 'items'|'even'|'wheel', status 'claiming'|'locked'|'settled', host_name text|null, host_monzo text|null, host_revolut text|null, host_sort_code text|null, host_account_number text|null, wheel_winner_id uuid|null, wheel_spun_at timestamptz|null, wheel_pay_to 'waiter'|'host', settled_at timestamptz|null, created_at timestamptz
- receipts: id uuid, bill_id uuid, label text, position int, service_mode 'none'|'add'|'included', service_rate numeric (0.125), service_included_pence int, receipt_total_pence int|null, discount_pence int|null
- items: id uuid, bill_id uuid, receipt_id uuid, name text, price_pence int (ONE unit; quantities are separate rows), position int
- guests: id uuid, bill_id uuid, name text, emoji text, color text, is_host boolean, has_phone boolean, in_wheel boolean (default true), paid_at timestamptz|null, created_at timestamptz
- claims: id uuid, bill_id uuid, item_id uuid, guest_id uuid, created_at timestamptz (unique per item_id + guest_id)
Mock data: the bill "Dishoom Kensington", code K7Q2, host Faizan, one receipt with service included £8.33 and receipt total £74.93, items Chicken Ruby 1590 · House Black Daal 990 · Lamb Biryani 1690 · Garlic Naan 450 · Garlic Naan 450 · Okra Fries 550 · Mango Lassi 550 · Masala Chai 390 (pence), and 3 guests Priya, Tom and the host with a few claims, including one shared item."""

seed_sql = """\
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
"""

p1 = quote(prompts, "### P1: UI Shell")
p1 = p1.replace(
    "[paste the §6 column lists for bills, receipts, items, guests, claims].", "\n" + COLUMNS + "\n\n"
).replace("[paste Appendix A]", "\n\n```ts\n" + split_ts + "```\n")
p1 = p1.replace("Design: [Prompt 0 design line].", DESIGN)

p3 = quote(prompts, "### P3: Receipt Photos")
p3 = p3.replace(
    "[paste §8 schema + instructions].",
    "\n\n```json\n" + reader_json + "```\n\nInstructions to the model: " + reader_rules + "\n",
)

TAIL = "Don't change files or behaviour not mentioned here."


def tail(text):
    """§9: every follow-up prompt ends with the no-tests line AND the scope line."""
    return text if TAIL in text else text.rstrip() + " " + TAIL + "\n"


files = {
    "00_project_knowledge.txt": quote(prompts, "### Prompt 0"),
    "01_P1_create_project.txt": p1,
    "02_schema.sql": schema_sql,
    "03_seed.sql": seed_sql,
    "04_P2_data_realtime.txt": tail(quote(prompts, "### P2: Wire Data")),
    "05_P3_receipt_photos.txt": tail(p3),
    "06_P4_modes.txt": tail(quote(prompts, "### P4: Modes")),
    "07_P5_polish.txt": tail(quote(prompts, "### P5: Polish")),
    "split.ts": split_ts,
}
for name, text in files.items():
    (OUT / name).write_text(text)
    print(f"{name:28} {len(text):6} chars")

leftover = [n for n, t in files.items() if "[paste" in t]
assert not leftover, f"unfilled placeholders in {leftover}"
