# Settld: the pitch

**Live app:** https://tabsplit-live.lovable.app · **Big screen:** host bar → 📺 Big screen
**One line:** *Settld splits the bill at the table and makes sure the host is paid before anyone stands up.*
**Close:** *Splitwise ends with an IOU. Settld ends with the host paid.*

---

## The features to highlight (in this order)

| # | Feature | Why judges care | Show it? |
|---|---|---|---|
| 1 | **Verified payments (YouMustPay)**: a card hold when you sit down, then **charged exactly your share**, the rest released, and **"Verified ✅ card"** from Stripe | Answers "how do you know they paid?" with proof, not trust. Nobody can leave without paying | ✅ The centrepiece |
| 2 | **Join in 5 seconds**: scan a QR or type a 4-letter code. **No app, no sign-up**, you get a silly name | The whole table can join, even judges | ✅ |
| 3 | **AI reads the receipt**: up to 4 photos, de-duplicates overlapping lines, puts service and discounts in their own fields, checks against the printed total | The "wow" at a Lovable AI event | ✅ |
| 4 | **"Say what you had"**: type or speak *"the lamb and half the daal"* and the AI ticks it, half share included | AI in every guest's hands | ✅ |
| 5 | **Penny-exact fair maths**: shared dishes split evenly, service charge shared in proportion to what you ate, totals always add up to the receipt | Trust in the numbers | Say it |
| 6 | **Money goes to the host**: Stripe Connect routes card payments straight to the host's bank. Or pay free by Revolut or bank transfer | Real payments, bank-neutral | Say it |
| 7 | **Spin for it 🎡**: card roulette, every phone spins at once and lands on the same person | Memorable, shareable | If time |
| 8 | **Live big screen**: QR, who's claimed what, who's paid | The room watches it fill up | ✅ (on the projector) |
| 9 | **Host tools**: Track screen, **WhatsApp chase**, **"You're owed £X"** across dinners, Mark paid for cash | Real-life follow-up | Say it |
| 10 | **AI table awards**: a funny roast receipt (Big Spender, Naan Hoarder…) | A guaranteed laugh | ✅ (it appears at Settled) |
| 11 | **Split evenly**, **people without a phone**, Apple Pay / Klarna / Revolut Pay at checkout | Covers every real table | Mention |

---

## Before you go on stage
- [ ] **Host device** (the one on stage) has **Stripe connected** (done in rehearsal). Step 3 should say **"Stripe connected ✅"**.
- [ ] Laptop on the projector. **Stripe Dashboard → Test mode → Payments** open in a tab for the proof moment.
- [ ] 2–3 teammates or judges ready to scan. **Each person's share needs to be under £40** (the hold), so use 2+ payers on the £74.93 demo bill.
- [ ] Optional: Stripe Dashboard → Settings → **Public details → business name "Settld"**, so checkout doesn't say "New business sandbox".
- [ ] Backup: a recording of the full loop on one phone.

## The 2-minute script

| Time | Do | Say |
|---|---|---|
| **0:00** | — | "Hands up if a group dinner ended with one person paying and then chasing everyone on WhatsApp for a week." |
| **0:15** | Host: **Start a table** | "This is Settld. You split the bill at the table, and the host is paid before anyone stands up. No app, no sign-up." |
| **0:25** | **Tonight's receipt** → items appear → step 3 **YouMustPay 🔒** → Open → **Big screen** | "The AI reads the receipt, even a long one across several photos, and checks it against the printed total." |
| **0:40** | Judges **scan** → silly names pop up → **Secure your seat** → **Apple Pay** | "Scan it. When you sit down, your card is held, just like a hotel. Nobody leaves without paying." 🔒 appears next to each name |
| **1:00** | One judge: **Say what you had** → *"the lamb and half the daal"*. Others tap | "Or just say what you ate. Shared dishes split to the penny, service and all." |
| **1:15** | Host: **🔒 Lock** → **Charge everyone 💳** | "Lock the bill, one tap, and everyone is charged exactly their share. The rest of the hold is released." Everyone flips to **Verified ✅ card** |
| **1:30** | Switch to the **Stripe Dashboard** tab | "And that's not a tick someone pressed. That's Stripe confirming the payment. In production it lands straight in the host's bank." |
| **1:40** | Back to the app: **Settled ✅** + awards | Read out one roast line |
| **1:50** | — | "Splitwise launched receipt splitting two weeks ago, so the problem is real. But it ends with an IOU. **Settld ends with the host paid.**" |

*If you have spare seconds:* ⚙️ More → **Spin for it** → Spin. "And some tables don't split, they spin."

## Q&A cheat sheet
- **How do you know they paid?** "Card payments are verified by Stripe: the hold, then the exact charge. If someone pays by bank transfer instead, the host confirms it."
- **Where does the money go?** "Stripe Connect sends it straight to the host's bank. We never hold anyone's money, Stripe is the regulated party. Tonight it's Stripe test mode."
- **How do you make money?** "A small fee on card payments, taken automatically through Stripe. Next is pay-by-bank, which is cheaper than cards, and then restaurants, who'd pay to have tables settle themselves."
- **Why a £40 hold?** "It covers a typical share. The host can change it, you're only ever charged your exact share, and the rest is released straight away."
- **Why not just use Splitwise?** "Splitwise records a debt. Settld collects it, at the table, with no app for anyone."
- **Isn't the wheel gambling?** "It's the card roulette friends already play, made fair and visible. Anyone can sit out, and no money comes to us."
- **Security?** "Tonight a table is a 4-letter code. In production: longer private links, and bank details replaced by pay-by-bank links."

## Fallbacks
- **Hold fails?** Switch the table to **Pay yourselves**: payers tap **Pay £X by card / Apple Pay** (Stripe Checkout) or **I've paid**, and the host taps **Mark paid**.
- **Nobody can scan?** Add `?demo=1` to the table link → **🎭 Simulate table** (say that you're using it).
- **Someone stuck on "Just watching"?** Pull down to refresh.
- **Wi-Fi dead?** Play the backup video.
