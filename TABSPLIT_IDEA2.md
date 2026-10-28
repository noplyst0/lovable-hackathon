# 🧾 Idea 2: TabSplit (Ready-to-Build Spec, v2)
**Theme:** Split a group restaurant bill item by item, and get the host paid before anyone stands up  
**Role in Hackathon:** ✅ The chosen build (SoftCircle, in `SOFTCIRCLE_IDEA1.md`, is the backup)  
**Time Limit:** 4 Hours (18:00 – 22:00) | **Target Event:** Lovable Buildathon, Imperial Entrepreneurs x YFL  
**Spec owner:** Claude (lead). Argon checks it at the points marked 🔍.

> v1 (Gemini's original proposal) is in git history. v2 keeps the core idea and fixes the facts that were wrong, adds what was missing, cuts what we shouldn't build, and adds the build prompts, SQL, maths and timetable.

---

## 0. Read This First: What Changed From v1

| # | v1 said | Reality / fix |
|---|---|---|
| 1 | "Splitwise forces all 8 people to download an app" | **No longer true.** On **14 Oct 2026** Splitwise launched **Itemize**, free in the **US and UK**: one person snaps the receipt and everyone else claims items by **QR with no app or account**, with proportional tax/tip. Several web tools (BillMath, BillTap, Divvi, SplitterUp) also do "QR, no download". **"No download" is no longer a wedge.** The positioning has to change (see §2). |
| 2 | "Calculates the 12.5% service charge **and VAT**" | UK menu prices **already include VAT**. Never add VAT. The only add-on is the discretionary service charge. |
| 3 | Service is always added at 12.5% | Many London receipts **already print the service charge** (always for groups of 6+). If we add it again, we double-charge the table. The receipt parser must detect it. |
| 4 | Long-press to split an item | Long-press can't be discovered on a phone. **Sharing = several people tap the same item**, and it splits equally between them. |
| 5 | "2x Garlic Naan" handled as one row | Each unit becomes **its own claimable row** (2× naan → two £3.50 rows). |
| 6 | `price numeric`, `(Item Total) * 1.125` | Money in floats drifts by pennies and totals won't match the receipt. **Store integer pence** and use a largest-remainder allocation so the shares always add up exactly. Tested code is in Appendix A. |
| 7 | "Affiliate kickbacks from Monzo/Revolut" | No public P2P affiliate scheme exists. Don't say it on stage. A more honest business story is in §2. |
| 8 | Revolut 1-click with amount | `revolut.me/<tag>` is documented, but **a pre-filled amount isn't**. Use a Monzo link with the amount filled in, Revolut's plain link, and a "Copy amount" button. |
| 9 | Not covered | Guest identity, the host being a diner too, OCR mistakes, unclaimed service, a demo reset, the published vs preview URL, realtime on DELETE. All covered below. |

---

## 1. The Idea (One Paragraph)
When the bill comes, the host snaps the receipt and AI turns it into a list of items in a few seconds. A QR code appears. Everyone scans it, types their first name, and taps what they had. Shared dishes split automatically between everyone who tapped them. The table screen fills in live: every item shows the faces of who claimed it, and anything nobody has claimed pulses red (*"Who had the garlic naan? 👀"*). Each phone shows that person's exact share, including their fair part of the service charge, with a **Pay [host] on Monzo** button that already has the amount filled in. When everyone has paid, the bill goes green. **The point is that nobody leaves owing the host money.**

---

## 2. Competitor Reality Check (Oct 2026) & Our Honest Wedge

| Who | What they do well | Where they stop |
|---|---|---|
| **Splitwise Itemize** (free in UK since 14 Oct 2026) | 50M+ users. QR claiming with no download. Proportional tax and tip. | The host needs Splitwise. Per launch coverage, it ends with Splitwise Pay (US), cash, or **an IOU added to a running Splitwise balance**. The debt is recorded, not settled. |
| **BillMath / BillTap / Divvi / SplitterUp** | Web QR splitters with no signup | Small and generic, mostly US-centric. No UK bank links, no "who's paid" view. |
| **Monzo / Revolut split** | Real money moves instantly | They split a *transaction*, so they can't read a paper receipt line by line. Per-person amounts are typed by hand. |
| **Sunday / me&u** | QR paying straight into the till | Only in venues that bought their system. |

**Our wedge, said honestly:** *"Splitting the bill is solved. Getting paid isn't."* Splitwise turns dinner into an IOU on a ledger. TabSplit is built around the moment at the table: a shared screen everyone watches fill up, UK bank payments with the amount filled in, live **paid ✅** ticks, and a bill that isn't "done" until the host is whole.

**Business story (keep it modest):**
1. **Growth:** every bill puts TabSplit in front of ~6 people who didn't install anything. Each guest is a future host.
2. **Revenue (to test):** venues pay for the "settled" screen, e.g. *"Back within 30 days? 10% off"*, shown at the moment of highest goodwill. Student societies' treasurers (they front the bill at every social) get a paid "Society" tier.
3. **Don't claim** neobank affiliate fees, a market size, or a take rate.

> If a judge says "Splitwise just launched this", **agree**: *"Yes, two weeks ago, which tells you the problem is real. Their answer ends with an IOU. Ours ends with the host paid before the waiter is back."*

---

## 3. Claude's Verdict

**Strengths:** the most relatable problem we have (every hand goes up), zero jargon, a live multi-phone demo, and a small, very buildable scope.  
**Weaknesses:** the "first to do it" story is gone (Splitwise). The business model is thin. Judges are seed VCs, who will think "feature, not company".  
**Net:** still a good hackathon build. The demo carries it, and the new positioning is defensible. **If business uniqueness turns out to be a big part of the judging rubric, SoftCircle is now the stronger pitch.** Its build is ~70% the same, so the switch stays cheap until 18:00.

| | Relatable | Demo wow | No jargon | Feasibility (×2) | Business | Judge fit | **/70** |
|---|---|---|---|---|---|---|---|
| TabSplit v1 (as written) | 10 | 8 | 10 | 8 (16) | 5 | 6 | 55 |
| **TabSplit v2 (this spec)** | 10 | 9 | 10 | 8 (16) | 4 | 6 | **55** |

*(The demo is better and the business is weaker after Splitwise's launch, so the total doesn't move.)*

---

## 4. Feature List

### 🟢 MUST (the demo doesn't work without these)
1. **Start a bill**, from either:
   - **"Use demo receipt"**: a pre-parsed seeded Dishoom bill. Always works, needs no AI and no Wi-Fi luck.
   - **"Snap receipt"**: the camera/photo upload calls the AI parser (§8).
2. **Host details:** host first name, Monzo username (optional), Revolut tag (optional). The host is also a guest and claims their own food.
3. **Review & fix screen:** edit name or price, delete, add an item. Shows *"Items add up to £X · receipt says £Y"* if they differ. Service setting: **Already on receipt (£X)** / **Add 10% / 12.5% / 15%** / **None**.
4. **Join:** QR + 6-letter code. The guest types **only a first name** and gets an auto colour/emoji. Their identity is kept in `localStorage` so a refresh doesn't create a duplicate.
5. **Claim:** tap to claim, tap again to unclaim. If several people claim one item, it splits equally. Other claimers show as avatar chips.
6. **Live sync** across every phone and the table screen (Supabase Realtime). On any change, refetch the bill and recompute.
7. **Correct maths:** integer pence, exact totals, service charged proportionally and never doubled (Appendix A).
8. **Table screen** (projector/laptop): items with claimer chips, **unclaimed items pulsing red**, a progress bar (*"£142.50 of £180.00 claimed"*), people with totals, and a big QR.
9. **Your share + pay** on the phone: a sticky footer with *"Your share £16.88 (incl. £1.88 service)"*, then **Pay on Monzo** (amount filled in), **Revolut** (plain link), **Copy amount**, then **"I've paid"**, which shows a ✅ on the table screen.
10. **Published URL in the QR.** Preview URLs may need a Lovable login, so the QR must point at the published app.

### 🟡 SHOULD (big payoff for little build)
11. **"Who had the …? 👀" banner** when only 1–2 items are left unclaimed.
12. **Everyone paid → confetti** and a big green "Settled ✅" on the table screen. This is the closing shot of the pitch.
13. **Lock bill** (host): freezes claims so amounts stop moving before people pay. Before it's locked, the pay sheet warns *"Bill not fully claimed yet, your share may change."*
14. **Host controls:** reset claims (between rehearsals), remove a guest, mark someone paid by hand.
15. **Simulate table** (hidden, `?demo=1`): 4 fake guests claim items with staggered delays. **Only used if the audience can't scan**, and say so out loud if it is.

### 🔵 STRETCH (only if everything above is done by 20:15)
16. **"Say what you had"**: a guest types *"the lamb and half the naans with Priya"* and Lovable AI ticks the items. A strong second wow moment that AI makes cheap, but it's another AI call that can fail.
17. Discount/promo lines spread across everyone automatically. In the MVP, the host edits prices instead.
18. Bills expire after 48h.

### 🔴 DON'T BUILD (time sinks, risks, or scope creep)
- Accounts, login or auth of any kind. The whole point is "type your name".
- Real payment processing (Stripe, Open Banking APIs). That's regulated, slow to set up, and a demo risk.
- Splitwise-style running balances, groups, history or friends.
- Multi-currency, VAT breakdowns, restaurant POS integration, a native app or PWA install.
- Long-press, drag-and-drop, custom % splits. Equal split among claimers covers 95% of dinners.
- Notifications, email, chat, comments.
- **Live OCR as the only path in the demo.** The seeded receipt is always one tap away.

---

## 5. Screens & Routes

| Route | Who | What |
|---|---|---|
| `/` | Host | Hero line *"Split the bill. Get paid before anyone stands up."* Buttons: **Snap receipt** / **Use demo receipt**. |
| `/new` | Host | Photo upload (or the demo receipt), host name, Monzo username, Revolut tag → creates the bill and the host guest. |
| `/b/:code/review` | Host | Edit items, check totals, choose service mode → **Open the table**. |
| `/b/:code` | Table screen | Built for **16:9 projector**, readable from 10m. Left: receipt items + chips + red pulse. Right: big QR + code, people list (avatar, name, total, ✅). Top: progress bar. Host controls behind a small ⚙️. |
| `/j/:code` | Guest phone | Name entry (first visit) → item cards (big tap targets) → "Still unclaimed" section on top → sticky footer with share + **Pay**. |

**Design direction:** "receipt paper", meaning an off-white background, ink-black text, prices in a monospace font, and one bold accent. Green = claimed, red pulse = unclaimed. Large type. Mobile-first for `/j`, projector-first for `/b`. **Don't** imitate Monzo's or Revolut's branding. Plain "Pay on Monzo" text buttons are fine.

---

## 6. Data Model (Lovable Cloud / Postgres)
Claude can run this directly through the Lovable MCP `query_database` tool (no build credits), or Lovable runs it as a migration from Prompt 1.

```sql
create table bills (
  id uuid primary key default gen_random_uuid(),
  code text unique not null,                 -- 6 chars, no 0/O/1/I
  restaurant_name text not null default 'Dinner',
  host_monzo text,
  host_revolut text,
  service_mode text not null default 'add' check (service_mode in ('none','add','included')),
  service_rate numeric not null default 0.125, -- used when mode = 'add'
  service_included_pence int not null default 0, -- used when mode = 'included'
  receipt_total_pence int,                   -- what the paper says, for the check
  status text not null default 'open' check (status in ('draft','open','locked','settled')),
  created_at timestamptz not null default now()
);

create table items (
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade,
  name text not null,
  price_pence int not null,                  -- one unit; quantities are exploded into rows
  position int not null default 0
);

create table guests (
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade,
  name text not null,
  color text not null,
  is_host boolean not null default false,
  paid_at timestamptz,
  created_at timestamptz not null default now()
);

create table claims (
  id uuid primary key default gen_random_uuid(),
  bill_id uuid not null references bills(id) on delete cascade, -- for realtime filtering
  item_id uuid not null references items(id) on delete cascade,
  guest_id uuid not null references guests(id) on delete cascade,
  created_at timestamptz not null default now(),
  unique (item_id, guest_id)
);

-- Realtime. REPLICA IDENTITY FULL so DELETE events (unclaim) still carry bill_id for the filter.
alter table bills  replica identity full;
alter table items  replica identity full;
alter table guests replica identity full;
alter table claims replica identity full;
alter publication supabase_realtime add table bills, items, guests, claims;

-- No accounts by design: anon can read/write. Bills are only reachable by their random code.
alter table bills  enable row level security;
alter table items  enable row level security;
alter table guests enable row level security;
alter table claims enable row level security;
create policy "public bills"  on bills  for all using (true) with check (true);
create policy "public items"  on items  for all using (true) with check (true);
create policy "public guests" on guests for all using (true) with check (true);
create policy "public claims" on claims for all using (true) with check (true);
```
> Lovable's security scan **will** flag these open policies. That's expected for a no-login hackathon MVP. Mention it if asked (§13).

**Demo seed:** one bill with code `DEMO42`, "Dishoom Kensington", ~8 items (Chicken Ruby, House Black Daal, Lamb Biryani, Garlic Naan ×2, Okra Fries, Mango Lassi, Chai), service included at 12.5%. **Swap in the real dinner receipt from the test run** if we have one.

---

## 7. The Split Maths (rules)
1. Everything is integer **pence**.
2. An item claimed by *k* people is split into *k* parts that add up exactly (leftover pennies go to the first claimers).
3. **Service total** = `round(items_total × rate)` if mode is `add`, the printed amount if `included`, otherwise 0.
4. Service is shared **in proportion to each person's food**, using the same exact allocation. Service on **unclaimed** items stays unallocated and shows in "remaining".
5. When everything is claimed, **sum of shares = receipt total, to the penny.** If not, it's a bug.
6. The host's own share is shown as *"Your part (you paid the restaurant)"*. No pay button for the host.

Reference implementation (tested): **Appendix A**. Claude pushes it as `src/lib/split.ts` through GitHub sync so Lovable doesn't have to write the maths.

---

## 8. Receipt Parsing (Edge Function `parse-receipt`)
- **Client:** resize the photo to ≤1600px JPEG, send base64 to the edge function.
- **Server:** call **Lovable AI** (built in, no API key) with a vision-capable Gemini model. Use **tool calling / a strict JSON schema**, not free text:
```json
{
  "restaurant_name": "string",
  "items": [{ "name": "string", "quantity": 1, "line_total_pence": 450 }],
  "service_charge_pence": 759,
  "receipt_total_pence": 6829
}
```
- **Instructions to the model:** prices in integer pence. `line_total_pence` is the price printed on that line. Ignore VAT summaries, card/payment lines, table numbers and "covers". If a service/"optional gratuity" line is printed, put it in `service_charge_pence` and **not** in items, otherwise null. Discounts are items with negative pence.
- **After the parse:** turn each line into `quantity` rows of `line_total/quantity` (spread leftover pennies). Set `service_mode = 'included'` if a service charge was found, otherwise `'add'` at 12.5%. Always land on the **review** screen.
- **If the parse fails or times out (>15s):** *"Couldn't read that one. Fix it by hand or use the demo receipt."* Never a dead end.
- Each parse uses Lovable AI usage from the same balance as credits. **Parse the demo receipt once in rehearsal and keep the result** as the seeded bill.

---

## 9. Lovable Build: Prompt Pack & Credit Budget

### Credits (8 credits is very tight, so read this)
- Per the Lovable MCP docs, **only `create_project` and `send_message` use build credits.** These don't: reading files/diffs, `query_database` (SQL), project knowledge, deploy. Neither do code pushed through **GitHub sync** or edits in Lovable's code editor. *(Confirm all of this in the test run.)*
- The message cost depends on complexity. A big prompt costs more than a small one but less than 4 small ones. **Plan: 3 build messages + 2 spares on the day.** Claude makes small fixes through GitHub, for free.
- **Ask the organisers whether attendees get Lovable credits** (buildathons usually hand out codes). If not, one month of Pro (~100 credits) is cheap insurance.
- **Test run budget: ≤3 credits.** Prompts 1 and 2 only, to measure the real cost per message and check the free paths.

### Prompt 0: Project Knowledge (free; set via MCP before Prompt 1)
> TabSplit: a no-login web app for splitting a restaurant bill item by item. Money is ALWAYS integer pence; never use floats for money and never add VAT (UK prices include it). Use the existing `src/lib/split.ts` for every money calculation; do not reimplement it. Guest identity is `localStorage` key `tabsplit:guest:<code>`. QR codes encode `window.location.origin + '/j/' + code`. Keep components small. Do not add auth, accounts, payments processing, or routes not in the spec. Design: receipt-paper off-white, ink-black text, monospace prices, green = claimed, pulsing red = unclaimed.

### Prompt 1: Foundation (1 message)
> Build TabSplit, a mobile-first web app for splitting a restaurant bill item by item. Enable Lovable Cloud. Create these tables exactly: [paste §6 SQL]. Seed bill `DEMO42` "Dishoom Kensington" with these items in pence: [list]. Service included 12.5%.
> Routes: `/` hero ("Split the bill. Get paid before anyone stands up.") with "Use demo receipt" (goes to `/b/DEMO42`) and "Start a bill" (`/new`, a form for host name, Monzo username and Revolut tag; creates a bill with a random 6-char code, adds the host as a guest with is_host=true, then goes to `/b/:code/review`). `/b/:code/review`: editable item list (name, price in £, delete, add), a check that shows "Items add up to £X, receipt says £Y", a service-mode selector (Already on receipt £ / Add 10, 12.5, 15% / None), and an "Open the table" button. `/b/:code`: a 16:9 table screen with items on the left (avatar chips of claimers, unclaimed items pulse red), on the right a big QR (qrcode.react) of `/j/:code`, the code in large type, and the list of people with totals and a ✅ when paid, plus a progress bar on top. `/j/:code`: if there's no guest in localStorage, ask only for a first name (assign a random colour); then show items as big tappable cards, where a tap inserts a claim and a second tap deletes it; "Still unclaimed" first; a sticky footer shows "Your share £X (incl. £Y service)".
> Realtime: on `/b/:code` and `/j/:code`, subscribe to postgres_changes on bills, items, guests and claims filtered by bill_id; on any event refetch the bill and recompute. Use optimistic updates for taps. All totals come from `computeSplit` in `src/lib/split.ts` [if it's not in the repo yet, create it with exactly this code: paste Appendix A].

### Prompt 2: Receipt Photos (1 message)
> Add "Snap receipt" to `/new`: a camera/file input that resizes the photo to max 1600px JPEG and sends it to a new edge function `parse-receipt`. The function uses Lovable AI with a vision Gemini model and tool calling to return exactly this JSON: [paste §8 schema + instructions]. Turn quantities into separate unit rows, set service mode as in §8, save items, and go to the review screen. On error or after 15s, show "Couldn't read that one. Fix it by hand or use the demo receipt." Don't change any other screen.

### Prompt 3: Pay & Polish (1 message)
> On `/j/:code` the sticky footer opens a sheet with: "Pay [host] on Monzo" (link `https://monzo.me/<host_monzo>/<amount>?d=TabSplit <restaurant>`; hide if no username), "Revolut" (`https://revolut.me/<tag>`, hide if none), "Copy amount", and an "I've paid" button that sets guests.paid_at. If the bill isn't locked, show "Bill not fully claimed yet, your share may change." The host guest sees "Your part (you paid the restaurant)" with no pay buttons. On `/b/:code`: show a banner "Who had the <item>? 👀" when 1–2 items remain unclaimed; when every non-host guest has paid, show full-screen "Settled ✅" with confetti (canvas-confetti); behind a ⚙️ button add Lock bill, Reset claims, Remove guest, Mark paid. With `?demo=1`, add a "Simulate table" button that adds 4 guests (Priya, Tom, Sam, Jess) who claim random unclaimed items with 1–2s delays. Don't change the maths or the data model.

### Spare messages (2)
Bug fixes Lovable is better at than a git push (layout, responsive issues). **Never use a credit to argue with a broken layout. Roll back instead** (§10, rule 2).

---

## 10. Workflow: Claude + Argon + Lovable

| Who | Role | Calls |
|---|---|---|
| **Claude** (lead) | Owns the spec, prompts, SQL, maths and git pushes. Reviews every Lovable output through MCP `read_file` / `get_diff` and checks the DB with `query_database`. | Continuous |
| **Argon** 🔍 | Critic/second opinion at fixed checkpoints only (usage limits). | ~4 calls total |
| **Lovable** | UI scaffolding, Cloud DB, Lovable AI, hosting. | 3 + 2 spare messages |
| **Humans** | Phones, real-world testing, the pitch. | Always |

**Argon checkpoints 🔍 (each one is a single prompt, so each is worth it):**
1. *Now:* "Red-team this spec: what breaks, what's missing, what would a judge attack?"
2. *After the test run:* review the bug list and the live app.
3. *20:30 on the day:* red-team the live demo flow and the failure plan.
4. *Pitch:* play a sceptical seed VC and grill us with the §13 questions.

**Golden rules**
1. **One big foundation prompt, then small, targeted ones.** With 8 credits, many tiny prompts are the expensive mistake.
2. **If Lovable breaks a layout, roll back.** Don't spend credits arguing with it.
3. **Lock features at 20:45.** After that it's only testing on phones and rehearsing.
4. Claude never edits a file Lovable is generating at the same moment (pull before every push).

---

## 11. Test Run Checklist (before the hackathon)
- [ ] Lovable MCP connected and authenticated. `list_workspaces` works.
- [ ] Cost of Prompt 1 and Prompt 2 in credits, written down here.
- [ ] `query_database` is free and can create/alter tables.
- [ ] A Claude push to the GitHub repo shows up in Lovable, costs no credits, and **edge functions redeploy** after a push (or not, so we know).
- [ ] Realtime works across 2+ phones on **4G and venue-style Wi-Fi**, including unclaim (DELETE).
- [ ] The QR opens the **published** URL on a phone that isn't logged in to Lovable.
- [ ] `monzo.me/<user>/<amount>?d=<note>` opens with the amount filled in (Monzo user AND non-Monzo phone).
- [ ] What `revolut.me/<tag>` does on a phone.
- [ ] Parse 3 real receipts (one with service printed, one with 2× items, one crumpled). Note what the AI gets wrong.
- [ ] Time a full loop with 4 people: scan → name → claim → pay → ✅. Target: under 60 seconds.

---

## 12. Hackathon-Day Timetable (18:00 – 22:00)
**Before 18:00:** this doc final, Monzo username ready, real receipt photo + expected items written down, phones charged, a hotspot as backup Wi-Fi, credits confirmed. Check the event rules: prompts written in advance are normally fine, but code built in advance may not be.

| Time | What | Credits |
|---|---|---|
| 18:00–18:15 | Claude: `create_project` with Prompt 1, set Prompt 0 knowledge, verify tables + seed via SQL, push `split.ts` | 1 |
| 18:15–19:00 | Fix what Prompt 1 got wrong (git pushes). **2 phones claiming DEMO42 live by 19:00.** | 0 |
| 19:00–19:40 | Prompt 2 (receipt photos). Test with the real receipt from tonight's food. | 1 |
| 19:40–20:20 | Prompt 3 (pay + polish). Publish. QR points at the published URL. | 1 |
| 20:20–20:30 | Spare message only if something big is broken. | 0–1 |
| 20:30–20:45 | 🔍 Argon red-teams the demo. Last fixes. | 0 |
| **20:45** | **🔒 Feature freeze** | |
| 20:45–21:15 | 5 phones, venue Wi-Fi AND 4G, full loop ×3. **Record a backup screen video** of a perfect run. | 0 |
| 21:15–22:00 | 🔍 Argon Q&A grilling. Rehearse the 2-minute pitch ×3 with a timer. Reset claims before going on stage. | 0 |

---

## 13. Demo & Stage Script (2 minutes)

**[0:00–0:25] Hook**
> *"Hands up if you've been at a group dinner and when the bill arrived, everyone went quiet?"* (Hands go up.) *"Twenty minutes of phone calculators. Someone says 'I didn't have wine'. Someone forgets the service. And one person puts their card down and spends the next week chasing friends on Monzo."*

**[0:25–1:05] The demo: judges are the dinner party**
> *"This is our receipt from the food tonight."* (Snap it live → items appear in a few seconds. **If the parse is slow, tap "Use demo receipt" and keep talking.**) *"Scan the code and tap what you ate."* (Wait 5s.) Point at the screen as chips appear: *"Shared the pizza? Tap it too, and it splits between you automatically, service charge and all, down to the penny."*

**[1:05–1:30] The laugh + the money**
> Point at the red pulsing item: *"And there's always one: who had the garlic bread? 👀"* *"Now look at your phone. That's your exact share, and one tap opens Monzo with the amount already filled in."* (One teammate pays for real → ✅ on screen.)

**[1:30–2:00] Why us + close**
> *"Splitwise launched receipt splitting two weeks ago, so the problem is real. But it ends with an IOU on a ledger. TabSplit ends with the host paid before the waiter's back. Every bill puts us in front of six new people who didn't install anything. TabSplit: get paid before anyone stands up."* (Settled ✅ + confetti if everyone paid.)

**Fallbacks:** audience can't scan → teammates' 3 phones + `?demo=1` Simulate table (*"here's what it looks like with a full table"*). Wi-Fi dead → play the backup video and narrate it.

---

## 14. Q&A Prep

* **"Doesn't Splitwise do this now?"** *"Since 14 October, yes, which validates the problem. Splitwise is a ledger: the result is a balance you settle later. We're built for the 5 minutes at the table: one shared screen, UK bank links with the amount filled in, and a bill that isn't done until the host is paid."*
* **"How do you make money?"** *"Honestly, we're consumer-first right now. Every bill is a free acquisition of ~6 people. The test is venues paying for the 'settled' screen, like a return-visit offer at the moment of highest goodwill, and a paid tier for society treasurers who front every social."*
* **"What if someone claims the wrong thing?"** *"Tap again to unclaim. And the table screen is in front of everyone, so mistakes get noticed. The host can lock the bill once everyone's happy."*
* **"How do you know someone actually paid?"** *"In this version it's self-reported plus the host's tick. Open Banking confirmation is the obvious next step, but we deliberately didn't touch real payment rails tonight."*
* **"Anyone with the link can edit, isn't that insecure?"** *"By design there are no accounts. Bills live behind a random code and are only useful for one dinner. Expiry after 48 hours is next."*
* **"What about the AI misreading the receipt?"** *"The host always gets a review screen with a check against the receipt total, so a misread is fixed in two taps before anyone sees it."*

---

## Appendix A: `src/lib/split.ts` (tested 28 Oct 2026)
Tested against: shared items, unclaimed items, exact totals with 12.5% added, service already printed on the receipt, empty bill, and the Monzo link format. Example: £60.70 of food + £7.59 service = **£68.29, and the three shares add up to exactly £68.29.**

```ts
// All money is integer pence. Never use floats for money.
export type Item = { id: string; price_pence: number };
export type Claim = { item_id: string; guest_id: string };
export type ServiceMode = "none" | "add" | "included";
export type Service = { mode: ServiceMode; rate: number; included_pence?: number };

// Split `total` across weights so the parts always sum to exactly `total` (largest remainder).
export function allocate(total: number, weights: Record<string, number>): Record<string, number> {
  const ids = Object.keys(weights).sort();
  const sum = ids.reduce((s, id) => s + weights[id], 0);
  const out: Record<string, number> = {};
  if (sum <= 0 || total === 0) { ids.forEach((id) => (out[id] = 0)); return out; }
  const raw = ids.map((id) => ({ id, exact: (total * weights[id]) / sum }));
  raw.forEach((r) => (out[r.id] = Math.floor(r.exact)));
  let left = total - raw.reduce((s, r) => s + out[r.id], 0);
  raw.sort((a, b) => (b.exact - Math.floor(b.exact)) - (a.exact - Math.floor(a.exact)) || a.id.localeCompare(b.id));
  for (const r of raw) { if (left <= 0) break; out[r.id] += 1; left -= 1; }
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
    for (const g of claimers) food[g] += parts[g];
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
    guest_id: g, food_pence: food[g], service_pence: svc[g] ?? 0, total_pence: food[g] + (svc[g] ?? 0),
  }));
  const billTotal = itemsTotal + serviceTotal;
  const claimedTotal = perGuest.reduce((s, p) => s + p.total_pence, 0);
  return { perGuest, unclaimed, billTotal, claimedTotal, remaining: billTotal - claimedTotal };
}

export const formatGBP = (p: number) => `£${(p / 100).toFixed(2)}`;
// TODO verify in test run: monzo.me/<username>/<amount>?d=<description>
export const monzoLink = (user: string, pence: number, note: string) =>
  `https://monzo.me/${encodeURIComponent(user)}/${(pence / 100).toFixed(2)}?d=${encodeURIComponent(note)}`;
```

## Sources
- Splitwise Itemize launch (14 Oct 2026, free in US & UK, QR claiming without the app): [The Paypers](https://thepaypers.com/payments/news/splitwise-launches-itemize-receipt-splitting-feature-in-the-us-and-uk), [Yahoo Finance](https://finance.yahoo.com/small-business/articles/splitwise-launches-feature-takes-awkwardness-123000659.html), [Digital Trends](https://www.digitaltrends.com/phones/splitwise-now-lets-you-calculate-everyones-share-of-a-restaurant-bill-including-tax-and-tip/)
- No-download web splitters: [BillMath](https://www.billmath.com/), [BillTap](https://billtap.app/), [Divvi](https://justdivvi.com/), [SplitterUp](https://splitterup.app/blog/best-receipt-scanning-apps)
- Lovable MCP server (tools; only `create_project` / `send_message` use credits): [lovablelabs/mcp](https://github.com/lovablelabs/mcp), [Lovable docs](https://docs.lovable.dev/integrations/lovable-mcp-server)
- revolut.me links (no documented amount pre-fill): [Revolut help](https://help.revolut.com/en-JP/help/transfers/payment-links/revolut-me-link/)
- Lovable credit pricing (secondary sources, check against lovable.dev): [eesel.ai](https://eesel.ai/blog/lovable-pricing), [UsagePricing](https://www.usagepricing.com/blueprint/activity/lovable-2026-10-05-chat-pricing-daily-allowance)
