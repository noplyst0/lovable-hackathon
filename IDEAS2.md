# 🚀 Hackathon Brainstorm Round 2 (IDEAS 2)
**Event:** Lovable Buildathon (Imperial Entrepreneurs x Young Founders London)  
**Location:** Sir Alexander Fleming Building, Imperial College London (18:00 – 22:00)

---

## 🎯 Goal for Round 2
Find **1–2 equally strong or superior backup options** that:
1. **Require ZERO startup/venture jargon to pitch** — You can speak 100% from your own personal experience without worrying about tricky investor terms or Q&A traps.
2. **Universal Audience & Judge Relatability** — Every single person in the room (student, professor, founder, investor) personally experiences the pain and laughs in agreement.
3. **Visually Irresistible Live Demo on Lovable** — A 10-second "Holy Cow" moment on the big projector.
4. **Realistic 4-Hour Scope** on React + Tailwind + Supabase.

---

## 💡 Gemini's Round 2 Proposals (Ideas 7–9)

### 🥇 Idea 7: "TabSplit" (or "FairShare") — The Real-Time Zero-Math Group Bill & Receipt Arbiter
* **The Problem (100% Relatable, 0% Jargon):** Everyone in London has suffered through group dinners (Nando's, Dishoom, birthday drinks). When the bill arrives, 8 people stare at a crumpled piece of paper for 20 minutes with phone calculators, arguing over who had drinks, who shared starters, and how to split the 12.5% service charge. It ends with someone awkwardly underpaying and one person eating the loss.
* **The 4-Hour Core Loop:**
  1. Take a photo of any receipt (or pick a sample restaurant bill).
  2. Gemini Vision extracts the itemized lines with prices in 3 seconds.
  3. A QR code appears: *"Scan to claim your items."*
  4. Everyone at the table scans with their phone. They see the menu items as clickable buttons.
  5. User taps *"Chicken Burger (£14)"* and taps *"Shared Fries (split 2 ways)"*.
  6. **The Magic Demo Moment:** The main screen live-allocates the receipt items in real time via Supabase Realtime:
     - Shows who claimed what.
     - Automatically calculates each person's exact share of tax and service charge.
     - Displays 1-click **Monzo / Revolut payment links** so people can settle up in 5 seconds.
* **Why It Wins:**
  - Zero financial or venture jargon. You pitch it like telling a funny story about dinner with friends.
  - Keeps the incredible live QR audience participation mechanic that judges love.
  - Solves a visceral, universal London pain point.

---

### 🥈 Idea 8: "ClauseCatch" (or "TrapDoor") — AI That Spots the Sneaky Traps in Your Tenancy & Job Contracts
* **The Problem (100% Relatable, 0% Jargon):** Students and young graduates sign tenancy agreements and employment contracts without reading 35 pages of legalese. Landlords slip in illegal deposit deductions (banned under the Tenant Fees Act 2019), and employers slip in predatory "IP Assignment" clauses (claiming the company owns anything you code on your laptop on weekends!).
* **The 4-Hour Core Loop:**
  1. Drop in a PDF or paste text of a tenancy agreement or employment contract.
  2. The AI audits the contract in 5 seconds against UK statutory tenant/worker protections.
  3. **The Magic Demo Moment:** The screen lights up with glowing red alert banners:
     - *🚨 RED FLAG: Clause 14 states the company owns all personal side-projects created on weekends (Overreaching IP clause).*
     - *🚨 RED FLAG: Clause 8 demands a £150 professional cleaning fee (Illegal under Tenant Fees Act 2019).*
     - *🚨 RED FLAG: Clause 22 requires 3 months notice for a 6-month contract.*
  4. Click **"Generate Diplomatic Pushback"**: The AI outputs an instant, polite, copy-ready email to the landlord or HR quoting the exact UK law to remove the clause.
* **Why It Wins:**
  - High social impact, emotionally empowering, zero complex jargon.
  - Every student renting in London or looking for tech jobs relates instantly.
  - Clean, high-polish dashboard with instant wow factor.

---

### 🥉 Idea 9: "VibePulse" (or "RoomTemp") — Real-Time Live Audience Temperature for ANY Presentation
* **The Problem (100% Relatable, 0% Jargon):** The universal, non-financial version of SoftCircle. When professors lecture, students give group presentations, or founders pitch, speakers have zero idea if the audience is engaged, bored, or confused until it's too late.
* **The 4-Hour Core Loop:**
  1. Speaker puts a QR code on the bottom corner of their slides.
  2. Audience scans on mobile: gets 3 fast, anonymous reaction buttons:
     - 🔥 *"Love this / Mind Blown"*
     - ❓ *"Lost / Explain This"*
     - ⚡ *"Pace up / Move on"*
  3. **The Magic Demo Moment:** As you talk on stage, animated reaction bubbles float up the screen live, and a glowing "Room Engagement Gauge" tracks audience temperature in real time.
* **Why It Wins:**
  - Dead simple to build and zero reliance on financial terminology.
  - Extremely fun for the audience to test live.

---

## 💡 Claude's Round 2 Proposals (Ideas 10–12)

### 🔬 Research First: What Actually Wins Hackathons (and What Judges Groan At)
I researched past winners (especially Lovable-hosted events) and judging guidance before proposing anything.

**Real Lovable hackathon winners:**
| Event | Winner | What it was | Lesson |
|---|---|---|---|
| Lovable × Project Europe, Stockholm (Aug 2025, €20k prize) | **Team Good Omen** (London engineers) | An AI journalist that conducts interviews and writes articles. A real media outlet (*Impact Loop*) **bought the tool on the spot** | Judges reward something a real customer would pay for *tonight* |
| SheBuilds on Lovable | **Puurfect** | A times-tables game with **live Kahoot-style multiplayer** for classrooms | Live, multi-phone participation wins rooms |
| Lovable AI Showdown (2025, $65k pool) | **RateSmart** (OpenAI track) | A review-management tool for chains: AI sorts customer reviews and drafts replies | Boring-but-useful business tools win too |
| Lovable-featured student hackathon | **MySafe** | A Waze-style community safety map | ⚠️ A safety map has *already been done* |

**What judges consistently say they reward** (Devpost / AngelHack / JetBrains judging guides):
1. **The problem is felt in the first 30 seconds.** Open with a specific human story, not market statistics.
2. **One flawless "happy path" beats ten half-built features.** A narrow slice that fully works is the most common trait of winners.
3. **Judges remember how a demo made them feel.** By pitch #15 they're exhausted; anything that makes them *do* something (scan, tap, laugh) is what gets remembered at deliberation time.
4. **A polished, projector-readable UI:** high contrast, zoomed in, big numbers.
5. **Always have a backup:** a pre-recorded 60-second video of the demo working, in case venue Wi-Fi dies.

**Ideas judges are tired of (avoid):** AI wellness/mental-health chatbots, "Uber for X" marketplaces, smart-city dashboards with fake data, generic budget trackers and e-commerce stores, and "AI roasts your CV" tools.

**Why money and everyday hassle work in this room:** Per Save the Student's 2025 National Student Money Survey, the Maintenance Loan falls **£502/month short** of average student living costs, and **61%** of students skip meals to save money. Everyday money and admin pain is something every student *and* investor instantly understands.

### 🤝 Convergence Note on TabSplit & ClauseCatch
Before seeing Gemini's Ideas 7 and 8, I had independently drafted almost the **same two ideas** (I called them "SplitSnap" and "Small Print"). Two models landing on the same ideas separately is a strong signal, so rather than duplicate them I've replaced mine with three different ideas below. My improvements to Gemini's versions:
* **TabSplit:**
  * Demo with **the team's real pizza receipt from tonight**. Make the judges the "dinner guests" who claim slices.
  * Make **one unclaimed item flash red** ("Who had the garlic bread? 👀"). It gets a laugh every time.
  * It shares ~70% of its build (QR code + phone tap screen + live host screen) with SoftCircle, which makes it the cheapest possible switch if we change plans.
* **ClauseCatch:**
  * Add a big **"This contract could cost you £X"** counter. A £ figure lands harder than a list of red flags.
  * Base the tenancy check on the actual Tenant Fees Act 2019 list of what landlords *are* allowed to charge: rent, a deposit capped at 5 weeks' rent, a holding deposit capped at 1 week, £50 for tenancy changes, and late-rent interest only after 14 days. That makes the flags accurate rather than guessed.
  * It's the only idea with **no audience or Wi-Fi dependency**, which makes it the safest demo.

---

### 🔹 Idea 10: "Sorted": Turns Your Chaotic Group Chat Into an Actual Plan
* **The One-Liner:** Paste or export your group chat. Sorted reads 200 messages of *"I'm free Saturday maybe?"*, works out the date, time and place that suit the most people (plus who's vegetarian, who can't do Sundays, and so on), then sends one link where everyone just taps ✅ or ❌.
* **Why everyone relates:** Every single person has a group chat where a plan died: a birthday dinner, a society social, a uni reunion, a team night out. Investors have it too, with co-investor calls and team dinners. It's the most universally recognised frustration on this list.
* **Pitch it with zero jargon:** *"Hands up if you're in a group chat right now where a plan has been 'happening soon' for three weeks."*
* **The 4-Hour Core Loop:**
  1. Paste chat text (WhatsApp's "Export chat" gives a .txt file) or screenshots.
  2. Lovable AI extracts each person's availability, constraints (diet, budget, area) and the options mentioned, as structured JSON.
  3. The **Plan Card** appears: the best slot, who can make it, who can't and why, and 2 AI-suggested venues.
  4. A QR code / share link opens an RSVP page where people tap their name and ✅/❌. The tally updates **live via Supabase Realtime**.
  5. Once enough people say yes: *"It's happening 🎉"*, plus a downloadable calendar invite (.ics file).
* **The Magic Demo Moment:** Put a painfully realistic, prepared group chat on the big screen: *"who's free?" / "depends" / "I can do Sunday but not after 6" / "wait which Sunday" / "can we do somewhere cheap"*. **The room laughs because everyone's lived it.** Click "Sort it". Five seconds later: *"Saturday 7:30pm · Dishoom Kensington · 7 of 8 can make it · Priya veggie ✅ · Tom can't do Sundays."* Then: *"You're all invited, scan and RSVP."* The live tally fills as the judges tap.
* **Business Story (if asked):** Venues and booking platforms pay a commission per group booking, and student societies or workplaces pay for organising socials. Honest weakness: WhatsApp has built-in polls, so the value is entirely in the AI reading the mess for you.
* **4-Hour Feasibility Score:** 8/10 (One structured AI call + a realtime RSVP page + a calendar file. Risk: long real chats, so cap the input at ~300 messages and use a prepared chat for the demo.)

---

### 🔹 Idea 11: "Overheard": Live Subtitles for Any Speaker, on Your Phone, in Your Language
* **The One-Liner:** The speaker talks. Everyone in the audience scans one QR code and reads **live subtitles on their own phone, in whatever language they choose**. If you're lost, tap "❓" and the speaker sees which sentence lost the room.
* **Why everyone relates:** Everyone has missed what a lecturer or speaker said because of bad acoustics, a fast talker, or a strong accent. International students (a large share of London's university population) follow every lecture in a second language. People who are hard of hearing get left out of most live events. Investors at international conferences have the same problem.
* **Pitch it with zero jargon:** *"Imagine every lecture you've ever attended had subtitles, in your language, on your phone."*
* **The 4-Hour Core Loop:**
  1. The presenter opens "Speaker mode" on a laptop. Chrome's built-in speech recognition (Web Speech API, free, no extra service needed) turns speech into sentences.
  2. Each finished sentence is saved to Supabase and broadcast live via Realtime.
  3. Audience phones: pick a language (English, 中文, Español, हिन्दी, العربية…). Each sentence is translated by Lovable AI and appears as a live caption feed.
  4. A "❓ Lost" button flags the current sentence. The speaker's screen shows a confusion spike. After the talk, everyone can get an AI summary in their language.
* **The Magic Demo Moment:** *"Scan this and pick any language you like."* As we keep pitching, the judges' phones subtitle us live in Mandarin, Spanish and Hindi. The big screen shows our words appearing in 5 languages side by side as we speak. It's a "how is that happening?" moment that also proves the product works in real time, with real speech.
* **Business Story (if asked):** Universities (who have accessibility duties under the Equality Act 2010) and conference organisers pay per event or per year. Honest weakness: Wordly and big-tech live captions exist; our edge is no app, no hardware, and it works on any phone in 10 seconds.
* **4-Hour Feasibility Score:** 6/10 (Speech recognition depends on a good mic and a quiet room, and translation adds ~1–2s of delay per sentence. Test with the actual venue mic. Fallback: play a pre-recorded audio clip into the laptop.)

---

### 🔹 Idea 12: "Ringer": An AI That Makes the Phone Calls You Hate Making
* **The One-Liner:** Tell Ringer what you need, e.g. *"Cancel my gym membership"*, *"Book a GP appointment"*, *"Dispute this parking charge"*, and an AI voice agent **phones the business for you**, handles the conversation, and sends you a summary of what was agreed.
* **Why everyone relates:** Everyone hates being on hold, the 8am GP appointment phone scramble, and gyms that make you *phone* to cancel. Gen Z famously avoids phone calls; busy investors don't have time for them. Voice AI agents are also one of the hottest areas VCs are backing right now.
* **Pitch it with zero jargon:** *"When did you last spend 40 minutes on hold? What if you never had to again?"*
* **The 4-Hour Core Loop:**
  1. User picks a task (Cancel subscription / Book appointment / Complain / Ask a question) and fills in details (name, membership number, the outcome they want).
  2. A Supabase Edge Function triggers an outbound call through a voice-agent API (e.g. **Vapi** or **ElevenLabs Conversational AI**). The agent introduces itself as an AI assistant calling on the user's behalf.
  3. The live transcript streams onto the screen during the call.
  4. Output: a summary card: *"✅ Membership cancelled. Final payment 1 Dec. Confirmation ref: GYM-4821."*
* **The Magic Demo Moment:** *"Can a judge give us their phone number? You're now the receptionist at a gym."* Click "Call". **The judge's phone rings in the room.** The judge answers on speaker and plays a stubborn receptionist ("Are you sure? We have a special offer…"). The AI politely but firmly insists while the transcript streams on the big screen, and it ends with the summary card. This is the single most memorable demo moment of every idea we've discussed.
* **Business Story (if asked):** Consumer subscription (~£5/month) or pay per call; later B2B for busy professionals and small businesses. Honest weakness: Google offers similar call assistants in the US, but nothing mainstream exists in the UK yet.
* **4-Hour Feasibility Score:** 5/10 (⚠️ The riskiest build: it needs a voice-agent account, a phone number and UK calling set up *before* the event, and venue noise or signal can break it live. Fallback: run the call as an in-browser voice conversation on speaker.)

---

## 🏆 Master Ranking: Top 5 Ideas Across Round 1 & Round 2

Here is how the top contenders compare when judged on **Demo Wow Factor**, **Ease of Pitching (Zero Jargon)**, and **Universal Relatability**:

| Rank | Project Name | What It Is | Why It Ranks Here | Jargon Level | Demo Wow Factor |
|---|---|---|---|---|---|
| 🥇 **#1** | **TabSplit** (Idea 7) | Real-time group restaurant bill & receipt splitter via QR | **The Safest & Most Relatable Slam Dunk.** Universal pain point, 0% jargon, keeps the live QR scan audience mechanic, zero VC knowledge required. | **None (0/10)** | **10/10** |
| 🥈 **#2** | **SoftCircle** (Round 1 Hybrid) | Live investor & founder demand capture for demo days | **The Highest Room & Event Fit.** Built specifically for pitch nights like tomorrow, but requires basic comfort with fundraising terms. | **Medium (5/10)** | **10/10** |
| 🥉 **#3** | **ClauseCatch** (Idea 8) | AI contract & tenancy trap detector with pushback email | **High Social Impact.** Incredible student utility, highly practical, zero jargon, but less live audience participation. | **Low (2/10)** | **8.5/10** |
| **#4** | **Claimable** (Idea 4) | GitHub commit history to HMRC R&D tax credit cash | **Strongest Fintech B2B Business.** Serious commercial value, but tax/AIF concepts are drier and less fun to demo. | **High (8/10)** | **8/10** |
| **#5** | **VibePulse** (Idea 9) | Live audience reaction & temperature gauge for talks | **Fun & Interactive.** Very easy to build, but feels more like a feature (like Slido) than a full standalone product. | **None (0/10)** | **8/10** |

---

## 📊 Claude's Ranking: My Ideas 10–12 vs the Top 2 Existing Ideas (SoftCircle & TabSplit)
Each idea is scored /10 on the Round 2 goals. **Feasibility counts double**, because the research is unanimous that a working demo beats an ambitious broken one.

| Rank | Idea | Relatable to everyone | Demo "wow" | Easy to pitch (no jargon) | Feasibility (×2) | Business story | Fits these judges | **Total /70** |
|---|---|---|---|---|---|---|---|---|
| 🥇 1 | **SoftCircle** (Round 1 winner) | 7 | 9 | 6 | 9 (18) | 8 | 10 | **58** |
| 🥈 2 | **TabSplit** (Gemini, Idea 7) | 10 | 8 | 10 | 8 (16) | 5 | 6 | **55** |
| 🥉 3 | **Sorted** (Claude, Idea 10) | 10 | 8 | 10 | 8 (16) | 4 | 6 | **54** |
| 4 | **Ringer** (Claude, Idea 12) | 10 | 10 | 9 | 5 (10) | 7 | 7 | **53** |
| 5 | **Overheard** (Claude, Idea 11) | 8 | 9 | 9 | 6 (12) | 6 | 7 | **51** |

**Why this order:**
1. **SoftCircle stays #1 for me, narrowly.** No other idea fits *this* room as well: the judges are investors at a pitch event, and the product *is* a pitch event. Its only real weakness is that it needs some startup vocabulary (covered by the cheat sheet in SOFTCIRCLE.md).
2. **TabSplit is the best backup.** Both models came up with it independently, everyone relates to it, it needs zero jargon, and it reuses SoftCircle's QR + live screen build. The weakness is that the business is less unique (Splitwise exists).
3. **Sorted** is just as relatable and funnier on stage, but has the weakest business story (WhatsApp polls exist).
4. **Ringer** has the best demo moment of all, but it's a 5/10 build risk. Only consider it if we set up the voice service tonight.
5. **Overheard** is impressive and has real social impact, but depends on live speech recognition in a noisy room.

**Where I disagree with Gemini:** Gemini ranks TabSplit above SoftCircle. On "can anyone pitch it confidently", Gemini is right. On "will seed VCs at a pitch night pick it", SoftCircle wins. **It comes down to your comfort level:** if pitching startup concepts on stage makes you nervous, make TabSplit the main idea. Either way, **agree the backup before 18:00** so there's no debate mid-sprint.
