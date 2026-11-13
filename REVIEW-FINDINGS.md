# REVIEW-FINDINGS — Design QA pass, 2026-11-12 (Claude)

## Current state

- Partner-review preview: https://fullyeqpd.github.io/heatcrafter/; the custom domain is not cut over.
- The repository contains 89 pages, including About Chimney Monkey, which explains the sister-company relationship.
- Phone and iPad layouts reflow below 1400px; wider desktop layouts retain edge-to-edge scaling.
- Both external Chimney Monkey footer mentions remain linked; the company column now also links to the new internal page.
- Both header/footer logos have brighter flames and illuminated original gold rays; brief ignition begins on first view, with still reduced-motion variants.
- Run `tools/prepare-site.py` and `tools/check-site.py` after every Pencil export.
- Existing form delivery, placeholder reviews, and product-copy questions remain separate prelaunch work.
- Art’s standing approval covers routine checked implementation, merge, and publication within scope.

## Log

### 2026-11-12 — Codex — Brighter original rays and matching footer glow

- Changed: brightened the flame/halo and illuminated the original ray pattern in both header and footer logos via a masked SVG overlay. Each logo animates on first view, then settles; hover/focus can replay it. Original PNGs and Pen source are unchanged.
- Check: verified full ray alignment, unique SVG IDs, footer first-view timing, nested-page mask URLs, reduced-motion positioning, and 320/820/1512px layouts. All 89 pages pass source/link checks; export reruns are idempotent; JS syntax/diff checks pass.
- Published: [PR #5](https://github.com/fullyeqpd/heatcrafter/pull/5) merged at `a4515cd`; GitHub Pages built successfully. Live verification confirms two overlays, correct mask URLs, header ignition, footer ignition on scroll, and no horizontal overflow. Next: preserve the shared export workflow in `NOTES-FOR-CLAUDE.md`.

---

### 2026-11-12 — Codex — Light the header logo’s flame

- Changed: added a decorative SVG flame, halo, and rays over the existing header mark via shared CSS/JS; the bear and lettering stay still. The effect plays for 3.6 seconds on load/hover/focus, then settles, with a still reduced-motion variant. Shared asset URLs now use content hashes.
- Check: original logo images and Pen artwork preserved; browser checks cover flame alignment, finite duration, reduced-motion behavior, and 320/820/1512px header sizing. Export reruns are idempotent, all 89 pages pass source/link checks, and JS syntax/diff checks pass.
- Published: [PR #4](https://github.com/fullyeqpd/heatcrafter/pull/4) merged at `99dfa27`; GitHub Pages built successfully and the live homepage loads the versioned script and runs the 3.6-second flame animation without horizontal overflow. Hover and keyboard replay were verified locally. Next: retain the combined export step documented in `NOTES-FOR-CLAUDE.md`.

---

### 2026-11-12 — Codex — Responsive layouts and sister-company page

- Changed: added shared phone/tablet reflow and touch navigation to all 89 pages; added `/about-chimney-monkey/` and its footer link. Updated the shared Pen Footer, added the sister page and phone/iPad hero references, and preserved existing desktop content.
- Check: 89 pages × 6 widths passed overflow/text-clipping checks, with 48 follow-up checks after table/page refinements. Menu navigation, Escape dismissal, footer routing, relative links/assets, export idempotency, and original-copy preservation passed; see `RESPONSIVE-QA.md`.
- Published: [PR #3](https://github.com/fullyeqpd/heatcrafter/pull/3) merged at `4597991`; GitHub Pages built successfully. Live phone homepage, iPad company/product layouts, touch navigation, and footer routing verified. Next: booking delivery and remaining prelaunch content; Claude should use the combined export helper and review new Pen references before re-exporting.

---

### 2026-11-12 — Codex — Footer partner links

- Changed: linked both footer mentions of Chimney Monkey to `https://chimneymonkey.com/` across all 88 pages, preserving the surrounding copy/layout. Added `tools/apply-footer-partner-links.py` and export guidance in `NOTES-FOR-CLAUDE.md` and `AGENTS.md`.
- Check: verified exactly 176 inline links and no other HTML changes; rerunning the helper changes zero pages. Browser click testing reaches Chimney Monkey. Claude: run both post-export helpers after future Pencil exports.
- Published: [PR #2](https://github.com/fullyeqpd/heatcrafter/pull/2) merged at `416c061`; GitHub Pages reports a successful build. The live homepage exposes both links, and clicking the published copyright link reaches Chimney Monkey. Genuine tablet/mobile layouts remain the next separate task.

---

## 2026-11-12 — Codex — Full-width preview published; standing approval clarified

- Changed: merged [PR #1](https://github.com/fullyeqpd/heatcrafter/pull/1) at `e3a2094` after Art's approval; the 88-page desktop width fix is published. Updated `AGENTS.md` to use Art's standing approval for routine implementation, verification, merging, and publishing within the requested scope without repeated permission questions.
- Check: GitHub Pages reports the merge commit built successfully. A fresh live homepage load at 1512px shows the page spanning x=0 to x=1511.99, zoom=1.05, and no horizontal overflow. The unversioned homepage initially served cached content; a deployment-version query returned the new build.
- Next: implement genuine tablet/mobile layouts as a separate task. The prior prepared-state entry is historical; this entry records the verified release. Initial domain cutover/noindex launch decisions and platform-required confirmations remain separate.

---

## 2026-11-12 — Codex — Desktop edge-to-edge preview prepared

- Changed: removed the 1440px upper scaling cap in all 88 index pages; the page expands proportionally to fill wider windows. Added `tools/apply-preview-fit.py`, export guidance in `NOTES-FOR-CLAUDE.md`, and Art's uppercase YOUR ACTION / NEXT STEPS communication preference in `AGENTS.md`.
- Check: all 88 HTML files differ only in the fit assignment; helper rerun changes zero pages. Browser checks at 390, 820, 1440, 1512, 1920, and 2560px show aligned page/header/footer edges and no horizontal overflow. Room, brand, product, and booking pages also fit at 1512px; the header booking link navigates correctly. Prepared on a review branch, not yet live.
- Next: approve the PR for publishing under the existing many-page review rule, then verify the deployed preview. Genuine tablet/mobile layouts remain separate work. Pen is now connected to the main HeatCrafter document; this fix belongs to the export script and required no canvas edits.

---

## 2026-11-12 — Codex — Shared Pencil and website design authority

- Changed: updated `AGENTS.md` at Art's explicit request so Codex and Claude can both edit Pencil designs, visual layouts, responsive behavior, exports, and implementation, including after launch; coordinated publishing uses the established workflow.
- Check: this supersedes the earlier Claude-only design role. Both agents should coordinate page/component ownership and serialize shared-document edits to preserve each other's work. Existing review entries remain unchanged.
- Next: the Pencil connector currently reports no running app connection, so canvas access is not yet verified. Desktop width and tablet/mobile layouts remain open work; no website source files changed in this documentation update.

---

## 2026-11-12 — Codex — GitHub integration write-access test

- Changed: added this documentation-only entry through the ChatGPT GitHub connector after Art authorized repository access for `fullyeqpd/heatcrafter` (repository ID `1307919133`).
- Check: this commit tests connector write access; all existing Claude review findings below are preserved. No HTML, CSS, JavaScript, images, or deployment settings are changed.
- Next: Claude can verify the single-file diff; this entry does not claim a new website QA pass or resolve earlier findings.

---

## Update 3 (infrastructure round): reconciliation with Codex's independent inspection

Codex's four reported findings, verified against deployed `main` (b504adc):

1. **"14 'ship free' instances outside /pro-tools/"** — STALE: measured before
   Art's 10:43 push. Deployed main now has **zero** cart/shipping terms outside
   /pro-tools/ (grep-verified against origin/main). No action.
2. **"No additional embedded Page/* frames"** — CONFIRMED, matches my result
   after the de-duplication pass.
3. **"Overflow 320–1440 not independently browser-verified"** — noted; my
   Playwright sweep covered all 88 pages × 5 widths, 0 issues. Independent
   re-verification welcome once Codex has write access to record results.
4. **"404.html redirects to /heatcrafter-site/"** — **REAL BUG, good catch.**
   An old 404 was resurrected by the August force-push flow and has shipped
   ever since. Fixed in this commit: 404.html now derives the preview root
   from the URL (works on any owner/org and later on a custom domain).

Also in this commit: AGENTS.md gains the four-collaborator role matrix
(Art / Claude / Codex / Charlie-planned). Codex write access and possible
repo transfer to a business org are in progress — see Art's action list.

---


## Update (same day): Art's decisions, executed

1. **Shopping cart removed** from the fireplace side (Art's call, 2026-11-12):
   "Add to Cart" → "Request a Quote", "Request Install Quote" → "Book a
   Showroom Visit", "Shop Now" → "Request Quote", spec-row "Free shipping /
   Ships free" → "Included in your quote", prose "ships free (to your door)" →
   "ships to your door" (drops the free-shipping promise, keeps the delivery
   fact). 32 files changed; zero cart terms remain outside `pro-tools/`.
   **Pro-tools "Buy Now" kept intentionally** (ships-nationwide pro corner).
2. **0% APR financing promo stays live** — financing runs through Chimney
   Monkey; revisit before launch.
3. **Reviews page**: parked; placeholder content stays for now.
4. **Dimplex Optimyst price normalized to $580** everywhere ($580.50 removed).

New Pencil-side items from this round (so re-exports don't regress):
- All cart-CTA/shipping copy changes above must be mirrored in the .pen files.
- Log-set product pages say "On live display in our Buffalo Grove showroom"
  (subtitle) AND "Available to order — may not be on the display floor" (badge)
  on the same page — contradictory availability signals; pick per product.

---


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
