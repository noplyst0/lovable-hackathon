# Build kit: fresh Lovable project at 18:00

Everything for the event lives in `~/Documents/Hackathons/lovable-tabsplit` (this repo, branch
`claude/focused-clarke-9f3jmy`). Generated from `TABSPLIT_IDEA2.md` by `python3 build/make_build_kit.py`.
**Edit the spec, then re-run; never hand-edit the generated files.** The morning "Tabsplit Test" project was
a personal test on the old v2 spec: don't reuse it. Its look (fonts + oklch colours) is pinned into P1.

**The only thing we're waiting on is hackathon credits.** Lovable workspace "Faizan's Lovable"
(G2UYdY6xk0J81iaqt0FU) is on the free plan until they land.

## 18:00 run sheet (Claude drives everything from this session via the Lovable MCP)

| Time | Step | File | How | Credits |
|---|---|---|---|---|
| 18:00 | Upload the 6 P1 attachments | `mockups/{pick,table,pay,track,wheel,screen}.png` | `get_file_upload_url` ×6 → `build/put_upload.sh <png> '<url>' '<user_id>'` | free |
| 18:01 | **P1** UI shell + attachments | `01_P1_create_project.txt` | `create_project` (workspace above, `files` = the 6 file_ids) → `render_project_widget` | ~5 |
| 18:01 | Project knowledge | `00_project_knowledge.txt` | `set_project_knowledge` | free |
| ~18:10 | DB on, schema, seed, verify select | `02_schema.sql`, `03_seed.sql` | `enable_database` + `query_database` | free |
| ~18:12 | Check P1: `get_diff`, `split.ts` byte-identical, screenshot | | `read_file`, `get_project` | free |
| 18:15 | **P2** data + realtime + lock/pay | `04_P2_data_realtime.txt` | `send_message` | ~5 |
| 19:00 | **P3** receipt photos, then score the reader with `assets/receipts/EXPECTED.md` | `05_P3_receipt_photos.txt` | `send_message` | ~4 |
| 19:35 | **P4** modes + wheel + no-phone person (re-attach `mockups/wheel.png`) | `06_P4_modes.txt` | `send_message` | ~5 |
| 20:10 | **P5** polish + demo safety, publish | `07_P5_polish.txt` | `send_message`, `deploy_project` | ~3 |
| 20:30 | 🔍 Argon red-team of the live app | | `agy -p … --model gemini-4-argon-high` | 0 |
| **20:45** | **🔒 Feature freeze** | | | |

- Upload URLs expire after 1 hour and files land in "ephemeral" storage, so upload right before the prompt
  (trial PUT verified at 16:33: HTTP 200).
- After every prompt: `get_diff`, and check `src/lib/split.ts` is still identical to `build/split.ts`.
- If Lovable pauses (`awaiting_input`), show Faizan the tool + params, then `respond_to_approval`. Never answer a
  pause with `send_message`.
- Escape hatch (§0): if P3 isn't working by 19:35, keep "Use demo receipt" + "Type it in" and go to P4.
- Never argue with a broken layout: roll back (free) and reword.

## Assets
- **Receipt test set** (`assets/receipts/`, Gemini 4 Argon): `lucky-dragon` (long; also `-part1`/`-part2` with 5
  overlapping lines), `nonna-rosa` (service + discount), `crown-anchor` ("2 x … @" lines, no service).
  Expected reader output: `EXPECTED.md`.
- **Backup stage receipt:** `assets/demo-receipt.png` (= the DEMO seed, £74.93).
- **Mockups:** `mockups/all-screens.png` (team overview), one PNG per screen for attachments, `screen.png` = the
  1280×720 big screen. Amounts are computed with `split.ts`.
- **Reviews:** `reviews/` (Argon's raw output; decisions are recorded in the spec).
