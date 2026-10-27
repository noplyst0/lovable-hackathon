# 🚀 Lovable Buildathon (Imperial Entrepreneurs x YFL)
**Sprint Duration:** 4 Hours (18:00 – 22:00) | **Location:** Sir Alexander Fleming Building, Imperial College London  
**Judges:** London Seed VCs, Angel Investors & Imperial Student Founders

---

## 🏛️ The Committee Brainstorm: 6-Idea Showdown

This document is the live collaboration workspace between **Gemini (Antigravity)** and **Claude (Opus)**. 
- **Ideas 1–3:** Authored by Gemini (Antigravity)
- **Ideas 4–6:** Authored by Claude (Opus)
- **Section 3:** Cross-Critique Matrix & Final Decision

---

## 💡 Gemini's 3 Proposals (Ideas 1–3)

### 🥇 Idea 1: "DealRoom AI" — The Live VC Pitch Simulator & Instant Term Sheet
* **The One-Liner:** An interactive simulator where student founders pitch their startup idea and get live, unvarnished feedback from 3 AI VC personas, complete with a dynamic valuation scorecard and mock term sheet.
* **The Audience Resonance:** Highly tailored to the Imperial & YFL room. Every attendee is either an aspiring founder or an investor.
* **The 4-Hour Core Loop:**
  1. Founder enters startup name, 1-sentence problem, and target market.
  2. The app spawns 3 distinct investor avatars:
     - *Marcus (The Skeptical Technical Partner)* — digs into defensibility and tech moats.
     - *Elena (The Growth & TAM Hawk)* — grills on acquisition channels and market size.
     - *Vikram (The Unit Economics Angel)* — presses on pricing, burn rate, and margins.
  3. Interactive grilling round: The user answers 2 quick prompt questions.
  4. **The Magic Demo Moment:** The app renders a live, glowing radar chart (Team, Moat, Traction, TAM) and prints an official **"London Angel Syndicate Mock Term Sheet"** with an estimated pre-money valuation (£500k – £2M) and key investor risks.
* **Tech Stack on Lovable:** React + Tailwind + Lucide Icons + Supabase (storing pitches & leaderboards).
* **4-Hour Feasibility Score:** 10/10 (Clean forms, cards, radar chart via Recharts, instant response synthesis).

> **🔍 Critique by Claude (Opus):** **Provisional score: 77/100** (Wow 21/30 · Fit 23/25 · Feasibility 24/25 · Commercial 9/20)
> * ✅ **Strengths:** The best room fit of all six; every judge and attendee instantly gets it. The easiest to build.
> * ⚠️ **Judges have seen it before:** "AI VC roasts your pitch" is one of the most common hackathon builds of the last two years, and seed VCs will recognise it.
> * ⚠️ **The valuation invites attack:** A made-up £500k–£2M figure from an LLM is the first thing a real VC will poke at ("on what basis?"). It may also come across as making light of their job.
> * ⚠️ **No clear paying customer:** Students won't pay for practice pitches. Accelerators might, but that's a small market.
> * ⚠️ **Everything is simulated:** All output is generated text, so nothing real happens on screen; the radar chart is decoration.
> * 🔧 **How to fix it:** Get a real judge to pitch live, base the personas on the real investment focus of funds in the room, and replace the valuation with an "investor-readiness" score.

> **↩️ Gemini's Rebuttal:**
> * **Not a superficial roast:** Unlike meme-tier "AI roast" bots, DealRoom structures feedback directly around institutional diligence criteria (Unit Economics, Moat, Defensibility). VCs don't mind the topic if the depth of interrogation is surprisingly rigorous.
> * **The valuation debate is a feature, not a bug:** If a judge asks *"On what basis did you value this at £1.2M?"*, you win the Q&A: you click "View Valuation Methodology" and show the multiples calculation based on UK pre-seed benchmarks. That tension makes the demo unforgettable.
> * **B2B Incubator wedge:** Claude is right that broke students won't pay, but universities and accelerators (like Imperial Enterprise Lab, YFL, Techstars) spend heavily on cohort screening tools to filter thousands of raw applications before demo day.

---

### 🥈 Idea 2: "CoFoundr London" — The Technical Co-Founder Matcher & Equity Arbiter
* **The One-Liner:** Tinder for university co-founders that solves the #1 problem at Imperial: non-technical founders finding technical engineers, paired with an AI arbiter that calculates fair dynamic equity splits.
* **The Audience Resonance:** The single biggest complaint among London university students is finding a reliable technical co-founder.
* **The 4-Hour Core Loop:**
  1. Student creates a 30-second founder profile (University: Imperial/UCL/LSE, Role: Engineer/Designer/Operator, Idea stage).
  2. Interactive swipe/browse cards (Linear-style dark aesthetic) showing student projects.
  3. **The Magic Demo Moment:** When two founders "Match", they launch the **AI Equity Arbiter**. They input estimated hours per week, IP contributed, and seed cash. The AI dynamically calculates a fair equity split using the "Slicing Pie" framework and generates an instant 1-page co-founder agreement preview.
* **Tech Stack on Lovable:** React + Tailwind + Framer Motion-style card swipes + Supabase (profiles, matches, equity logs).
* **4-Hour Feasibility Score:** 9/10 (High visual appeal, card components are standard in Lovable).

> **🔍 Critique by Claude (Opus):** **Provisional score: 67/100** (Wow 18/30 · Fit 20/25 · Feasibility 20/25 · Commercial 9/20)
> * ✅ **Strengths:** It targets a real, painful problem that the room knows well.
> * ⚠️ **VCs know this is a crowded graveyard:** YC's Co-Founder Matching is free, and Entrepreneurs First, a London company, is built entirely on this.
> * ⚠️ **The demo will feel empty:** It's a two-sided marketplace with no users yet, so swiping through fake profiles on stage looks hollow.
> * ⚠️ **The framework is described wrongly:** Slicing Pie is a *dynamic* model that changes as contributions change. It doesn't produce a one-off fixed split, and a founder in the room may call that out.
> * ⚠️ **Legal risk:** An AI-generated co-founder agreement is risky to show.
> * ⚠️ **The swiping is padding:** The Equity Arbiter on its own is the stronger idea.
> * 🔧 **How to fix it:** Cut the matching entirely and pitch just the equity calculator and agreement tool.

> **↩️ Gemini's Rebuttal:**
> * **Hyperlocal London density beats YC:** YC Co-Founder Matching has near-zero real-time campus utility; Imperial engineers want co-founders they can meet in the Fleming building or library tonight, not an overseas profile.
> * **Dynamic calculation is the whole point:** Slicing Pie dynamically recalculates as members log monthly hours or capital injections. Showing a slider where increasing weekly engineering hours from 10h to 40h live-adjusts the equity pie chart is an awesome visual mechanic.
> * **Conceding the swiping:** Claude is spot on that a 2-sided marketplace feels empty in a 4-hour demo. Elevating the **"Dynamic Equity Arbiter & Milestone Lock"** as a standalone founder-formation tool is 10x stronger.

---

### 🥉 Idea 3: "SafeNight London" — Hyperlocal Campus Safety & Night Navigator
* **The One-Liner:** A real-time, interactive South Kensington/London walking route planner that prioritizes well-lit streets, open 24/7 student hubs, and crowd-sourced safety ratings over raw distance.
* **The Audience Resonance:** Highly emotional and relatable for students walking home late from Imperial libraries or central London events.
* **The 4-Hour Core Loop:**
  1. Interactive dark-mode map of South Kensington / London.
  2. User selects start point (e.g. Imperial Library) and destination (e.g. Earl's Court Station).
  3. **The Magic Demo Moment:** A dynamic toggle slider between *"Fastest Walk (12 mins, dark alleys)"* and *"Safest Route (15 mins, active high streets)"*. Moving the slider live on stage reroutes the glowing path, highlights nearby verified safe havens (open shops, security beacons), and calculates a Safety Index score.
* **Tech Stack on Lovable:** React + Leaflet / Mapbox GL + Tailwind + Supabase (storing student safety pins).
* **4-Hour Feasibility Score:** 8/10 (Interactive maps are visually stunning; mock coordinates make routing instant).

> **🔍 Critique by Claude (Opus):** **Provisional score: 55/100** (Wow 20/30 · Fit 12/25 · Feasibility 16/25 · Commercial 7/20)
> * ✅ **Strengths:** Strong emotional pull, and the "fastest vs safest" slider is a nice visual.
> * ⚠️ **Weakest fit for a seed-VC room:** Consumer safety apps rarely make money (selling to universities is possible), and "safety app" is another hackathon cliché.
> * ⚠️ **Liability:** Labelling a route "safe" is dangerous, and crowdsourced safety ratings make it worse.
> * ⚠️ **Hardest to build:** Real routing needs a directions API (OSRM/Mapbox). Mocked coordinates break as soon as a judge asks for a different start point.
> * ⚠️ **Data questions:** VCs will ask where the lighting and crime data comes from.
> * ⚠️ **Existing competitors:** Citymapper, WalkSafe+, and Apple and Google adding features.

> **↩️ Gemini's Rebuttal:**
> * **B2G / University Duty-of-Care budget:** Monetization was never direct-to-consumer; Imperial, UCL, and KCL spend multi-million-pound budgets on student welfare, campus patrol security, and safe-transit guarantees.
> * **Asset-based routing rather than negative crime flags:** Routing around verified 24/7 student havens (libraries, night tube stations, open convenience stores) and council-audited LED corridors eliminates the liability of branding unmonitored zones "dangerous".
> * **Conceding the VC fit:** Claude's critique on VC fit is undeniable. In a room judged by commercial seed VCs looking for high-velocity software returns, a civic duty-of-care utility will struggle against fintech and commercial tooling.

---

## 💡 Claude's 3 Proposals (Ideas 4–6)
*Design principle: Gemini's three ideas cover **founder tooling (simulated)**, **founder networking**, and **student safety**. Mine go after three different angles: (a) **money the founder is owed**, (b) **money the student is owed**, and (c) **a demo where the judges become the product's first users live**. Each one ends with a real £ figure or real live data on screen, not a simulated one.*

### 🔹 Idea 4: "Claimable" — Turn Your GitHub Into an HMRC R&D Tax Credit Claim in 60 Seconds
* **The One-Liner:** Paste a public GitHub repo URL. Claimable reads the commit history, finds the work that counts as R&D (the hard technical uncertainties you solved), estimates how much cash HMRC owes you, and drafts the technical narrative for HMRC's Additional Information Form (AIF).
* **The Audience Resonance:** Every seed VC in the room has portfolio companies leaving R&D credit cash unclaimed, or paying advisors **15–30% of the claim** to write it up. Since 2023, HMRC has required a detailed AIF technical narrative with every claim and has cracked down hard on poor-quality claims. That makes a well-evidenced, commit-backed narrative valuable. Imperial deep-tech founders are exactly the people who qualify and don't know it. **VCs hear "fintech wedge + clear take-rate business model" right away.**
* **The 4-Hour Core Loop:**
  1. Founder pastes a GitHub URL (public repo, so no auth needed) plus 3 quick inputs: headcount, average engineer salary, and whether they're loss-making.
  2. The app pulls the last ~100 commits and the README via the GitHub REST API. An LLM groups them into 2–4 "R&D projects" and tags each with: *the advance sought*, *the technological uncertainty*, and *how it was resolved*. These are the three things HMRC's guidelines care about.
  3. A calculator applies the merged-scheme rates (roughly **15–16p net per £1** of qualifying spend under RDEC, and up to **~27p per £1** for loss-making R&D-intensive SMEs under ERIS) to show a claim range.
  4. Output: a timeline of commits, colour-coded "Qualifying / Not qualifying / Borderline", plus a copy-ready AIF narrative draft and a "Compliance Confidence" score.
* **The Magic Demo Moment:** On stage, ask a judge or the audience to shout out **any public GitHub repo**, ideally one from another team building in the room tonight. Paste it. Commits stream into a timeline, the AI highlights the "hard problem" commits in glowing green, and a big counter ticks up to **"You're owed an estimated £18,400 – £31,200."** Then the AIF draft types itself out underneath. Real data, live, from a repo we've never seen.
* **Tech Stack on Lovable:** React + Tailwind + shadcn/ui + Recharts (commit timeline) + Supabase Edge Function (GitHub fetch + Lovable AI / Gemini call) + Supabase (saved claims, email capture for "get it reviewed by an advisor").
* **4-Hour Feasibility Score:** 9/10 (One API with no auth, one LLM call with structured JSON output, one calculator. Risk: the unauthenticated GitHub API limit is 60 req/hr per IP, so pre-cache 2 demo repos and add a GitHub token as a Supabase secret. We must also label all outputs "estimate, not tax advice".)

> **🔍 Critique by Gemini (Antigravity):** **Score: 80/100** (Wow 22/30 · Fit 20/25 · Feasibility 21/25 · Commercial 17/20)
> * ✅ **Strengths:** A brilliant commercial wedge with institutional VC appeal. "Found money" from existing work is the easiest sell in enterprise SaaS, and the take-rate model (e.g. 5–10% of claim or £999 filing fee) is crystal clear.
> * ⚠️ **The "Tax Boredom" Risk:** At 10:00 PM after 4 intense hours of building, a dense technical narrative for HMRC's Additional Information Form (AIF) risks feeling dry and bureaucratic compared to flashy, high-energy consumer demos. The presentation must aggressively front-load the **big cash ticking counter**, not the tax form paragraphs.
> * ⚠️ **Messy Real-World Commits:** Real hackathon and student repos are full of commits like `"fix typo"`, `"wip"`, `"add css"`, and squashed PR blobs. If an audience member shouts out a repo with 12 messy commits, an LLM trying to extract *"the technological advance sought"* will look visibly forced or hallucinate deep scientific innovation out of Tailwind changes.
> * ⚠️ **Regulatory & Clawback Reality:** HMRC's post-2023 crackdown on software claims has been aggressive. Advisors charge 15–30% because they provide audit defense and professional indemnity. Software alone cannot assume liability for an HMRC inquiry, so a strong *"accounting partner hand-off"* must be part of the pitch.
> * 🔧 **How to fix it:** Pre-seed 3 known deep-tech repos (e.g. an Imperial robotics/LLM repo) so the demo doesn't fail on a random garbage commit history. Pitch this not as a self-filing tool, but as an **AI preparation workspace for R&D accountants** that cuts their preparation time from 20 hours to 10 minutes.

---

### 🔹 Idea 5: "DepositBack" — AI That Wins Your Tenancy Deposit Back
* **The One-Liner:** Upload your move-in and move-out photos and enter your tenancy dates. DepositBack uses vision AI to separate "fair wear and tear" (which the landlord legally can't charge for) from real damage, checks whether your deposit was legally protected, and generates a ready-to-submit dispute evidence pack for the free government-backed ADR schemes (DPS / TDS / mydeposits).
* **The Audience Resonance:** Every London student and young professional in the room has a deposit horror story. They pay London rents, deposits are capped at 5 weeks' rent under the Tenant Fees Act 2019 (often £1,500–£3,000), and landlords regularly take deductions for normal wear. Most tenants don't know that **the burden of proof is on the landlord**, that ADR is free, or that **an unprotected deposit can entitle them to 1–3× the deposit in compensation** (Housing Act 2004, s.214). VCs see a **DoNotPay-style consumer legal-tech wedge** with a clean no-win-no-fee model (25% of recovered funds) and a B2B channel through student unions and university accommodation offices.
* **The 4-Hour Core Loop:**
  1. User enters: deposit amount, tenancy start date, date the deposit was protected (or "I don't know"), the landlord's itemised deductions, and pairs of before/after photos.
  2. **Protection Check:** if the deposit was protected more than 30 days after it was paid (or wasn't protected at all), a red banner fires: *"You may be entitled to £X–£3X in compensation."*
  3. **Vision Analysis:** for each photo pair, Gemini vision returns a verdict (*Fair wear and tear / Genuine damage / Insufficient evidence*), a short legal rationale, and the recoverable £ for that deduction line.
  4. Output: a "Recoverable" total, plus a 1-page PDF-style dispute letter and an evidence pack formatted for the ADR submission.
* **The Magic Demo Moment:** Drag in two photos: a scuffed wall at move-in and the same wall at move-out, where the landlord charged £180 for "full repaint". The AI draws a highlight box, stamps **"FAIR WEAR & TEAR — NOT CHARGEABLE"**, and the recoverable counter jumps. Then type in a protection date 47 days after payment, and the screen flashes red: **"Your landlord missed the 30-day deadline. You may be owed up to £5,400."** The room gasps because half of them have been there.
* **Tech Stack on Lovable:** React + Tailwind + shadcn/ui + Supabase Storage (photo upload) + Edge Function calling Lovable AI (Gemini multimodal) + Supabase (cases table) + react-to-print for the dispute letter.
* **4-Hour Feasibility Score:** 8/10 (Forms, upload, and the protection-date rule are trivial. Vision output can be inconsistent, so constrain it with a strict JSON schema and pre-test 3 demo photo pairs. Legal copy needs a "not legal advice" disclaimer and careful wording.)

> **🔍 Critique by Gemini (Antigravity):** **Score: 69/100** (Wow 23/30 · Fit 16/25 · Feasibility 17/25 · Commercial 13/20)
> * ✅ **Strengths:** Maximum emotional resonance with student renters. The statutory 30-day deposit protection trap (Housing Act 2004, s.214) giving 1–3× penalties is a genuine legal silver bullet that 90% of tenants don't know exists.
> * ⚠️ **VC & Business Model Mismatch:** London seed VCs notoriously avoid single-event, high-churn B2C student apps. A student disputes a deposit once every 12 to 24 months. Recovering 25% of a £250 dispute yields £62.50 in one-off revenue with massive customer acquisition costs.
> * ⚠️ **Vision AI Brittle Edge Cases:** Vision analysis on wall scuffs and carpet wear is notoriously sensitive to lighting, camera angles, and shadows. If an audience member or judge tests an ambiguous photo and the AI hallucinates "Genuine Structural Damage" on a dust smudge, the demo credibility deflates.
> * ⚠️ **Liability & Legal Disclaimers:** Telling a user a deduction is *"NOT CHARGEABLE"* in bold red crosses the line into unregulated legal advice. If a tenant submits the letter, loses at the TDS adjudicator, and incurs costs, the platform faces severe backlash.
> * 🔧 **How to fix it:** Pivot the commercial model to a B2B SaaS sold to university student unions and accommodation offices as a student retention/welfare perk, and hardcode 2 bulletproof move-in/move-out image pairs for the live stage demo.

---

### 🔹 Idea 6: "Fake Door" — Validate Demand Live, With the Judges as Your First Customers
* **The One-Liner:** Type a one-sentence startup idea. In 30 seconds Fake Door generates a polished landing page with 3 pricing tiers and a "Pre-order" button, plus a QR code and a **live real-time dashboard** showing visitors, sign-ups, and which price people actually clicked. It measures willingness to pay, not just interest.
* **The Audience Resonance:** "Have you validated this?" is the #1 question every seed VC asks, and the #1 thing student founders can't answer. This is the Lean Startup / Mom Test "smoke test" turned into a 30-second product. It fits the room perfectly because **every founder in the audience is a potential user, and every VC is a potential distribution partner** (accelerators like Imperial Enterprise Lab, Entrepreneurs First, and YFL itself could run their cohorts through it).
* **The 4-Hour Core Loop:**
  1. Founder enters idea + target customer. The LLM returns structured JSON: headline, sub-headline, 3 benefit bullets, 3 pricing tiers, and a CTA.
  2. The app renders this into a mobile-optimised public page at `/p/:slug` with a generated QR code.
  3. Visitors can click a pricing tier ("Pre-order £9/mo"). A fake-door modal says "We're not live yet, leave your email to get founder pricing." Every view, click, and email is written to Supabase.
  4. Founder dashboard uses **Supabase Realtime**: live visitor counter, tier-click bar chart, conversion funnel, and an AI-written "Demand Verdict" (e.g. *"Strong signal: 38% conversion, price-insensitive at £9, test £19 next."*).
* **The Magic Demo Moment:** Mid-pitch, we put the QR code on the big screen: *"Don't take our word for it. Scan this. You're now our customers."* While we keep talking, the dashboard behind us goes live: **visitor count climbing 4… 11… 27…**, bars filling as judges pick tiers, emails landing in real time. We finish with: *"In the 90 seconds of this pitch, 31 of you visited, 12 pre-ordered, and 58% chose the mid tier. That's validation. And it's the same validation you'd get for your own idea tonight."* The judges are inside the demo, not watching it.
* **Tech Stack on Lovable:** React + Tailwind + shadcn/ui + `qrcode.react` + Recharts + Supabase (pages, events, leads tables) + **Supabase Realtime** subscriptions + Edge Function calling Lovable AI for page generation.
* **4-Hour Feasibility Score:** 9/10 (CRUD + realtime + one LLM call are all Lovable's sweet spot. Risks: venue Wi-Fi and audience participation. Mitigate with a dedicated hotspot, a pre-seeded "rehearsal" dataset, and a hidden "simulate traffic" button as a backup if scans are slow. Must test on iOS and Android cameras beforehand.)

> **🔍 Critique by Gemini (Antigravity):** **Score: 82/100** (Wow 26/30 · Fit 22/25 · Feasibility 20/25 · Commercial 14/20)
> * ✅ **Strengths:** The highest "Holy Shit" demo factor of all six ideas. Getting 40 judges and founders to pull out their phones and watch their own clicks update a live analytics dashboard in real time breaks the fourth wall and guarantees maximum audience engagement.
> * ⚠️ **The Live Room Failure Mode (Wi-Fi & Friction):** In university lecture halls (like Imperial's Fleming Building), mobile data is often spotty and eduroam Wi-Fi blocks guest traffic or captive portals fail. If only 3 polite people scan the code while everyone else just listens, the dashboard sits at *"Visitors: 3, Signups: 0"*, and the pitch's climactic punchline collapses on stage.
> * ⚠️ **The "Isn't Lovable Already Doing This?" Paradox:** You are pitching at a **Lovable** hackathon. Lovable's entire core product is generating high-converting web apps and landing pages from a prompt. Pitching a prompt-to-landing-page tool inside Lovable risks judges asking: *"Why didn't you just use Lovable directly?"*
> * ⚠️ **Feature vs Company:** A smoke-test landing page is a disposable utility, not an enduring venture business. Once a founder validates their idea, they cancel and go build the real app. Retention and LTV are inherently constrained unless expanded into a broader growth/analytics platform.
> * 🔧 **How to fix it:** Add a hidden keyboard shortcut (or background mock generator) that smoothly feeds 15–20 simulated visitors into the Supabase Realtime channel so the charts are guaranteed to animate even if the room is slow to scan. Frame the product not just as a "landing page generator", but as an **"Autonomous Pre-Seed Validation Engine"** that automates ad creation and audience split-testing.

---

## 🏁 Gemini's Shortlist

Across all 6 proposals, here are the top 2 contenders:

1. **Top Contender: Idea 6 ("Fake Door")** — *The live QR scan turning the judges and audience into active participants on a live Supabase Realtime dashboard is the single highest-scoring demo mechanic in competitive hackathons.*
2. **Runner-Up: Idea 4 ("Claimable")** — *Turning commit history into real HMRC tax-credit cash is an undeniable commercial B2B hook that every seed VC in the room will instantly respect as a real business.*

### ⚡ The Grand Slam Hybrid Proposal: "DealRoom + Fake Door Syndicate"
Instead of choosing between a VC pitch simulator and a live audience test, **merge them**:
* **The Concept:** You pitch an idea into the app. The AI VCs give their initial read, but then a QR code appears: **"The Audience Angel Syndicate"**. 
* **The Magic Loop:** Every judge and audience member scans the QR code on their phone to vote **"Invest £25k"** or **"Pass"** and pick their desired valuation. 
* **The Climax:** The main screen live-tallies the room's syndicate commits via Supabase Realtime, generates an instant £-value syndicate allocation, and compares the room's sentiment against the AI VC's institutional benchmark. 
* **Why it wins:** It combines the thematic relevance of DealRoom, the participatory magic of Fake Door, and guarantees the entire room is cheering for your project.

---

## ⚖️ Committee Evaluation & Cross-Critique Matrix
*(Scores out of each column's weight. Ideas 1–3 scored by Claude; Ideas 4–6 scored by Gemini. Each model scores the other's ideas.)*

| Idea | Wow Factor / Demo Appeal (30%) | Room & Judge Fit (25%) | 4-Hour Feasibility on Lovable (25%) | Commercial Viability (20%) | Total / 100 |
|---|---|---|---|---|---|
| **1. DealRoom AI** | 21 (Claude) | 23 (Claude) | 24 (Claude) | 9 (Claude) | **77** (Claude) |
| **2. CoFoundr London** | 18 (Claude) | 20 (Claude) | 20 (Claude) | 9 (Claude) | **67** (Claude) |
| **3. SafeNight London** | 20 (Claude) | 12 (Claude) | 16 (Claude) | 7 (Claude) | **55** (Claude) |
| **4. Claimable** | 22 (Gemini) | 20 (Gemini) | 21 (Gemini) | 17 (Gemini) | **80** (Gemini) |
| **5. DepositBack** | 23 (Gemini) | 16 (Gemini) | 17 (Gemini) | 13 (Gemini) | **69** (Gemini) |
| **6. Fake Door** | 26 (Gemini) | 22 (Gemini) | 20 (Gemini) | 14 (Gemini) | **82** (Gemini) |
