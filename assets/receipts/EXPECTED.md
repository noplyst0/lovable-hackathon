# Test receipts: what the reader should return

AI-generated with Gemini 4 Argon (High) on 28 Oct (one chat each, Gemini usage 0% → 6% of the window), plus the
HTML-rendered demo receipt. **Each image's printed text was checked by eye: all three match their prompt exactly,
every line and every total.** Use these to score the `parse-receipt` edge function (§8) after P3.

Multi-photo test: `lucky-dragon-part1.jpg` + `lucky-dragon-part2.jpg` are the long receipt cut in two. The
5 lines Egg Fried Rice → Jasmine Tea (Pot) appear in BOTH photos; the reader must return them once (still 14 lines).

Pass = every line item found exactly once with the right `quantity` and `line_total_pence`, service and
discount in their own fields (never items), VAT / card / subtotal lines ignored, and the total correct.

## 0. `../demo-receipt.png`: Dishoom Kensington (the DEMO seed, rendered from HTML)
| name | qty | line_total_pence |
|---|---|---|
| Chicken Ruby | 1 | 1590 |
| House Black Daal | 1 | 990 |
| Lamb Biryani | 1 | 1690 |
| Garlic Naan | 2 | 900 |
| Okra Fries | 1 | 550 |
| Mango Lassi | 1 | 550 |
| Masala Chai | 1 | 390 |

service 833 · discount null · total 7493 · items 6660 → **8 unit rows**. Review check: 6660 + 833 = 7493 ✅

## 1. `lucky-dragon.png`: LONG receipt (also cut into 2 overlapping photos to test multi-photo)
| name | qty | line_total_pence |
|---|---|---|
| Salt & Pepper Squid | 1 | 850 |
| Pork Gyoza | 2 | 1300 |
| Crispy Duck (Half) | 1 | 2200 |
| Char Siu Bao | 1 | 680 |
| Beef Ho Fun | 1 | 1350 |
| Kung Pao Chicken | 1 | 1290 |
| Mapo Tofu | 1 | 1050 |
| Egg Fried Rice | 2 | 900 |
| Garlic Pak Choi | 1 | 720 |
| Singapore Noodles | 1 | 1180 |
| Tsingtao | 3 | 1650 |
| Jasmine Tea (Pot) | 1 | 450 |
| Coke | 2 | 700 |
| Mango Pudding | 1 | 590 |

service 1864 · discount null · total 16774 · items 14910 → **19 unit rows**. Review check: 14910 + 1864 = 16774 ✅
Traps: "Subtotal", "VAT 20% included", "Paid by card" must not become items. Multi-photo: no line counted twice.

## 2. `nonna-rosa.png`: service printed AND a discount
| name | qty | line_total_pence |
|---|---|---|
| Margherita | 1 | 1150 |
| Diavola | 1 | 1350 |
| Quattro Formaggi | 1 | 1400 |
| Burrata | 1 | 950 |
| Garlic Bread | 1 | 550 |
| Tiramisu | 1 | 700 |
| Peroni | 1 | 580 |
| Sparkling Water | 1 | 350 |

service 791 · **discount 703** · total 7118 · items 7030 → 8 unit rows.
Expected app behaviour: Review shows "Receipt has a £7.03 discount: edit prices to apply it", and the check line
reads 7030 + 791 = 7821 ≠ 7118 until the host knocks £7.03 off the prices. The discount must never be a negative item.

## 3. `crown-anchor.png`: "2 x … @" quantity lines, NO service printed
| name | qty | line_total_pence |
|---|---|---|
| Cheeseburger | 2 | 2590 |
| Fish & Chips | 1 | 1550 |
| Pint Camden Hells | 3 | 1860 |
| Halloumi Fries | 1 | 650 |
| Sticky Toffee Pud | 2 | 1350 |

service null · discount null · total 8000 · items 8000 → **9 unit rows** (1295×2, 620×3, 675×2).
Traps: the "@ 12.95" unit price must not be read as the line total, and "VISA contactless 80.00" must not become an item.
Expected app behaviour: service_mode = 'add' 12.5% by default, so the check line reads £90.00 vs £80.00 until the
host picks **None** (the receipt says "Service not included").
