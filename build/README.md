# Build kit: fresh Lovable project at 18:00

Generated from `TABSPLIT_IDEA2.md` by `python3 build/make_build_kit.py`. **Edit the spec, then re-run; never
hand-edit the generated files.** The morning project "Tabsplit Test" was a personal test on the old v2 spec:
don't reuse it, but its look (fonts + oklch colours) is pinned into P1 so the new build matches it.

| Time | Step | File | Tool | Credits |
|---|---|---|---|---|
| 18:00 | P1 UI shell (optionally attach `mockups/*.png` as design references) | `01_P1_create_project.txt` | `create_project` (workspace G2UYdY6xk0J81iaqt0FU) | ~5 |
| 18:00 | Project knowledge | `00_project_knowledge.txt` | `set_project_knowledge` | free |
| ~18:10 | DB on, schema, seed, verify select | `02_schema.sql`, `03_seed.sql` | `enable_database` + `query_database` | free |
| 18:15 | P2 data + realtime + lock/pay | `04_P2_data_realtime.txt` | `send_message` | ~5 |
| 19:00 | P3 receipt photos, then score with `assets/receipts/EXPECTED.md` | `05_P3_receipt_photos.txt` | `send_message` | ~4 |
| 19:35 | P4 modes + wheel + no-phone person | `06_P4_modes.txt` | `send_message` | ~5 |
| 20:10 | P5 polish + demo safety, publish | `07_P5_polish.txt` | `send_message`, `deploy_project` | ~3 |

After every prompt: `get_diff` and check `src/lib/split.ts` is still byte-identical to `build/split.ts`.
Escape hatch (§0): if P3 isn't working by 19:35, keep "Use demo receipt" + "Type it in" and go to P4.

**Receipt test set** (`assets/receipts/`): `lucky-dragon` (long; also cut into `-part1`/`-part2` with 5 overlapping
lines), `nonna-rosa` (service + discount), `crown-anchor` ("2 x … @" lines, no service). Backup stage receipt:
`assets/demo-receipt.png` (= the DEMO seed, £74.93).
