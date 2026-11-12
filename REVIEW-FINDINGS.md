# REVIEW-FINDINGS — Design QA pass, 2026-11-12 (Claude)

Full review of all 88 pages per Art's QA brief. Automated sweep: every page at
1440 / 1024 / 768 / 390 / 320 px — horizontal overflow, JS errors, accordion
function, nav-target resolution, local image resolution. Visual inspection: one
page per template type at full resolution. Newest entries on top.

## Fixed in this pass (in the generated-page layer; Pencil cleanup still owed)

| # | Severity | Issue | Fix | Verified |
|---|---|---|---|---|
| 1 | **Critical** | 20 pages contained entire OTHER pages embedded below their footer (15 product pages ×1 extra, 4 Real Fyre vented pages ×2 extras, 4 pro-tools pages ×1). Cause: page frames overlap on the Pencil canvas, and the Aug export swept in overlapping neighbors. Duplicate content, double/triple page weight, "Add to Cart" blocks surfacing on quote-only pages. | Foreign `Page/*` subtrees removed; fixed-height canvas wrappers collapsed to true page height. | All 20 re-swept at 5 widths, 0 issues; doc height == page height. |
| 2 | **High** | `/financing/` rendered 380px of blank space above the header (export captured empty canvas above the frame). | Re-flowed page to top. | Page top = 0, sweep clean. |
| 3 | Medium | `/fireplace-insert/gas-fireplace-insert/` claimed "8 models · 4 brands" and "Showing 8" over a grid of 6 models from 2 brands. | Copy corrected to 6 · 2. Other catalog pages audited — counts honest. | Grep-verified. |
| 4 | Low | Page titles "Stuv 16 / Stuv 6 / Stuv — HeatCrafter" missing the û. | Titles now "Stûv …". | Grep-verified; body text was already consistent. |

**Pencil-side cleanup owed (so future re-exports don't regress):** separate the
overlapping page frames on the canvas (the 20 affected product/pro-tools frames
plus whatever sits 380px above Page/Financing). Until then, any re-export of
those pages must repeat the de-duplication.

## Decisions needed from Art

1. **"Add to Cart" / "Shop Now" / "Free shipping"** appear on the homepage, 9
   log-set/electric/water-vapor product pages, and the schedule page's
   Currently Burning strip. Pro-tools "Buy Now" is intentional (ships-nationwide
   pro side). For the fireplace side this is the open hybrid-commerce decision
   from July: keep cart CTAs for shippable items (log sets, electric, water
   vapor) or switch everything to Request Quote.
2. **Financing "0% APR for 3 months" is live** on /financing/ (hero band +
   monthly-financing card). Lender and disclosures were still undecided in
   July. Fine for partner preview; must be resolved or removed before launch.
3. **Reviews page content is placeholder** presented as real ("4.9 across 120+
   reviews on Google, Facebook & Houzz", named reviewers with dates). Same for
   the three homepage testimonials. Fine as mockup; MUST be replaced with real
   reviews (or clearly reduced claims) before launch — this was an explicit
   criticism of the old site.
4. **Dimplex Optimyst price appears as $580 (29×) and $580.50 (8×).** Which is
   right? One normalization pass once Art confirms.
5. **Stûv model naming**: both "Stûv6/Stûv16" and "Stûv 6/Stûv 16" appear in
   body copy (4 each). Pick one (suggest "Stûv 6"); fix in Pencil.
6. **Claims to confirm as business promises** (all plausible, none fixed by me):
   "every gas unit we sell includes a safety screen"; "NFI-certified
   installation"; "Chimney Monkey pulls the permit" (town pages); "every price
   is fixed after a free site visit"; showroom "Burning in our display room"
   badges on Chaska 29 / Split Oak Designer Plus / Optimyst Aura (CMS-toggle
   design — confirm current lineup); hours Mon–Sat 10–6; vent-free IL wording.
7. **About page owner card says "Photo coming soon"** — a real photo of Art and
   real showroom/install photos remain the biggest trust gap (also flagged in
   the original site review).

## Known-and-accepted (no action this round)

- No responsive layouts: phones/small windows get the scaled 1440px page
  (by design until the mobile-design project).
- 237 Unsplash hotlinks: fine for preview; self-host before launch.
- Catalog cards for models without product pages (Enviro E30/S30, Chaska 34,
  Mendota D30/FV44i/ML39) are not clickable — either add pages or accept.
- Filter chips and "Load More" buttons are static mockups.
- "Crew orders" text in the pro-tools dark band clips at the right page edge
  mid-word — Pencil fix (band width/padding).
- Room-page hero paragraph contrast over bright window areas is marginal but
  readable; optional scrim deepen in Pencil.

## Readiness verdict

**Ready for partner review after this pass is published** — the duplicate-page
contamination was the one genuine blocker and is fixed. Items 1–3 above should
be answered before partners are told to look closely at pricing/financing/
reviews, and items in "Decisions" block launch but not review.

— Claude (via Art's Cowork session). Codex: the 24 changed files in this
commit are all in the generated layer; AGENTS.md rules unchanged.
