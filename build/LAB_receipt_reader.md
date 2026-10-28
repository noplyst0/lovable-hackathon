# Teammate lab: test the AI receipt reader (own Lovable account, own project)

**Goal:** by ~19:15, tell Faizan whether Lovable AI reads our test receipts correctly. If it does, the main build adds
photos with confidence. If it doesn't, we skip photos and save 20 minutes. Don't touch the main TabSplit project.

## 1. Start a new Lovable project and paste this as the first message

```
Build a one-page test tool called "Receipt Reader Lab". Enable Lovable Cloud and Lovable AI. No login, no storage bucket, no other pages.

Page: a file input that accepts up to 4 images at once (accept="image/*" multiple). Resize each to max 1600px JPEG on a canvas and keep it as a full data:image/jpeg;base64,... data URL (if one can't be decoded, read the original file as a data URL with FileReader). Show the thumbnails in order, a "Read receipt" button, and a stopwatch showing how many seconds the read took.

Create the edge function parse-receipt, called with supabase.functions.invoke; it must work without login (verify_jwt = false). It uses Lovable AI, the built-in gateway with LOVABLE_API_KEY (do not ask me for any API key), with the vision model google/gemini-2.5-flash (or the current Gemini Flash if that's retired). Send all photos in ONE request as image_url parts with the data URLs, and use tool calling that returns exactly:
{ "restaurant_name": "string", "items": [{ "name": "string", "quantity": 1, "line_total_pence": 450 }], "service_charge_pence": 833, "discount_pence": null, "receipt_total_pence": 7493 }

Instructions to the model: "These photos are parts of ONE receipt, in order, and may overlap. Return each line item exactly once: if a line appears in two photos, include it once." Prices are integer pence and line_total_pence is the printed line price (for "2 x Burger @ 12.95  25.90" that's quantity 2 and 2590, never the @ unit price). Ignore subtotal, net and VAT summaries, payment/card lines, table numbers and covers. A printed service/"optional gratuity" line goes in service_charge_pence, never in items (null if none). Discounts go in discount_pence as a positive number, never in items (null if none).

Results area: the raw JSON, a table of items (name, quantity, line total in £), and a check line: "items £A + service £B − discount £C = £D vs receipt total £E" in green if D equals E, red if not. On error or after 20 seconds show the error message. Don't write tests or run browser checks.
```

If Lovable asks to enable Cloud or AI, say yes.

## 2. Test these 5 cases (download the images from GitHub)

Images: https://github.com/noplyst0/lovable-hackathon/tree/claude/focused-clarke-9f3jmy/assets
(click an image → the download button at the top right).

| # | Upload | Pass if |
|---|---|---|
| 1 | `demo-receipt.png` | 7 lines (Garlic Naan qty 2 = 900), service 833, total 7493, check line green |
| 2 | `receipts/lucky-dragon.png` | 14 lines, Pork Gyoza qty 2, Tsingtao qty 3, service 1864, total 16774, green |
| 3 | `receipts/lucky-dragon-part1.jpg` **and** `-part2.jpg` together | still exactly 14 lines (5 lines appear in both photos), green |
| 4 | `receipts/nonna-rosa.png` | 8 lines, service 791, **discount 703** (not an item), total 7118, green |
| 5 | `receipts/crown-anchor.png` | 5 lines, Cheeseburger qty 2 **2590** (not 1295), service **null**, total 8000, green; "VISA" is not an item |

Full expected answers: `assets/receipts/EXPECTED.md` in the repo.

## 3. Report to Faizan
For each case: pass/fail, seconds taken, and what was wrong. A screenshot of any failure is perfect.
