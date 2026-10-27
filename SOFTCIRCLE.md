# 🚀 SoftCircle — Project Blueprint & Pitch Guide
**Event:** Lovable Buildathon (Imperial Entrepreneurs x Young Founders London)  
**Location:** Sir Alexander Fleming Building, Imperial College London  
**Time Limit:** 4 Hours (18:00 – 22:00) | **Repo:** `https://github.com/noplyst0/lovable-hackathon`

---

## 📖 1. The Startup Basics (Plain-English Cheat Sheet)

If you've never been to a venture pitch event, here are the simple terms so you feel 100% confident:

* **What is a "Deck" (Pitch Deck)?**  
  A 10-slide presentation explaining a startup's problem, solution, market size, and team. Investors review it before deciding to write a check.
* **What is an "Angel Investor"?**  
  A wealthy individual (often a former founder) who invests their **own personal money** (£5k to £50k) into early-stage startups.
* **What is a "VC" (Venture Capitalist)?**  
  An investment firm managing a fund (millions of pounds) raised from big institutions to back fast-growing startups.
* **What is a "Demo Day" (Pitch Night)?**  
  An event where 10–20 startup founders pitch on stage for 2–3 minutes each to a room full of angels, VCs, and fellow founders.
* **What does it mean to "Soft-Circle" money?**  
  When an investor likes a pitch, they don't immediately wire cash on stage. They give an informal, non-binding verbal pledge: *"Put me down for £10,000."* In venture capital, that verbal promise is called **"soft-circling"** money.

---

## 🛑 2. The Problem We Are Solving

At every demo day in the world (Techstars, Y Combinator, Imperial Enterprise Lab, YFL pitch nights):
1. Founders pitch on stage.
2. Investors in the audience whisper, scribble on napkins, or think *"I'd back that"*.
3. **Over 80% of investor interest vanishes the moment pitches end.** 
4. Founders spend weeks chasing people on LinkedIn, while organizers have zero organized data on who in the room liked what.

---

## 💡 3. What is SoftCircle?

> **"SoftCircle is the real-time investor demand & pledge-tracking platform for startup demo days."**

Think of it as **"Kahoot meets AngelList for live venture pitch events."**

It connects the **big presentation projector** directly to **every smartphone in the room** in real time.

---

## 📱 4. How the App Works (The Two Screens)

### Screen 1: The Main Stage Projector (Presenter View)
* **Header:** *"Now Pitching: Team 4 — CleanEnergy AI"* (or whatever startup is on stage).
* **Center Screen:** A large, high-contrast **QR Code** that says *"Scan with your phone to Soft-Circle or Support"*.
* **Live Realtime Counters (Powered by Supabase Realtime):**
  * 💰 **`£125,000 Soft-Circled (7 Investors)`**
  * 🚀 **`44 Founder Upvotes & Beta Signups`**
* **Live Sentiment Bar:** Shows real-time feedback tags (*Team: 88% · Market: 72% · Traction: 65%*).

---

### Screen 2: The Mobile Voter Screen (What the Audience Sees on Their Phones)
When someone scans the QR code, **they do NOT need an account or password**. They land directly on a fast, 1-tap card:

```
┌──────────────────────────────────────────────────┐
│             🔥 NOW PITCHING: SoftCircle          │
├──────────────────────────────────────────────────┤
│                                                  │
│   👔 IF YOU'RE AN INVESTOR / ANGEL:              │
│   [ 🟢 Soft-Circle £5k ]  [ 🟢 Soft-Circle £10k ] │
│   [ 🟢 Soft-Circle £25k ] [ ⚪ Request Deck ]     │
│   [ 🔴 Pass ]                                    │
│                                                  │
│   🚀 IF YOU'RE A FOUNDER / STUDENT:              │
│   [ ⭐ Upvote Startup ] [ 🙋 Want Beta Access ]   │
│   [ 🤝 Offer Mentorship / Intro ]                │
│                                                  │
│   (Optional) Leave your email or LinkedIn:       │
│   [ email@example.com             ] [ Submit ]   │
└──────────────────────────────────────────────────┘
```

---

## 🎪 5. The "Magic Demo Moment" (What We Do on Stage)

This is the exact sequence that wins the hackathon:

1. **Step 1 (The Hook):** Walk up and address the room directly:
   > *"Right now in this room, great founders will pitch, and people in the back rows will think 'I'd put £10,000 into that.' But after tonight, notes get lost, and 80% of that momentum disappears."*
2. **Step 2 (The Call to Action):** Put the QR code on the big projector:
   > *"We built SoftCircle to capture live venture momentum in real time. Pull out your phones and scan the screen right now. If you're an angel, soft-circle a ticket. If you're a student founder, hit Upvote or Beta Access."*
3. **Step 3 (The Magic Moment):**
   * The audience points their cameras at your slide.
   * People tap buttons on their phones.
   * **Instantly, the big projector screen behind you updates live without refreshing:**
     `£0 → £35,000 → £85,000 → £140,000 Soft-Circled`  
     `Upvotes: 4 → 12 → 31 Founders`
4. **Step 4 (The Close):**
   > *"In the 60 seconds of this pitch, 28 of you soft-circled £140,000 and 31 requested early access. This isn't just an idea—we just captured real investment interest for ourselves, live on your screen."*

---

## 💰 6. The Business Model (Who Pays?)

When the judges ask: *"Who buys this?"*
* **The Primary Buyer:** **Event Organizers & Accelerators** (Imperial Enterprise Lab, YFL, Techstars, Seedcamp, Angel syndicates).
  * They run dozens of pitch events annually and pay **£500 to £1,500 per event** (or £5k/yr SaaS) because SoftCircle automates investor follow-ups and proves the value of their cohort.
* **The Secondary Buyer:** **Founders**, who can pay a small fee to unlock direct contact info and analytics on which investors pledged interest.

---

## 🛠️ 7. The 4-Hour Build Plan on Lovable

* **18:00 – 18:30:** Create Lovable project, connect GitHub, set up 3 Supabase tables (`events`, `startups`, `votes`).
* **18:30 – 19:30:** Build the Mobile Voter Screen (responsive Tailwind card, 1-tap buttons, no login required).
* **19:30 – 20:30:** Build the Main Stage Presenter Dashboard (`qrcode.react` generator + Supabase Realtime live counter + Recharts bar).
* **20:30 – 21:15:** Test the live loop: scan with phone, tap £10k, verify screen updates in 0.5s.
* **21:15 – 22:00:** Add the hidden "Simulate Traffic" shortcut (as a backup if venue Wi-Fi is spotty) + practice the 2-minute pitch.

---

## 🛡️ 8. Legal & Compliance Note (To Impress Seed VCs)
At the bottom of the presenter dashboard, display this small discreet note:
> *"Non-binding indications of interest (IOI) only. Not an offer or solicitation of securities under UK FSMA 2000."*  
*This shows the judges that you understand UK financial promotions law and aren't running an illegal unlicensed broker!*
