# HeatCrafter Preview Site — Agent Guide

This repo is the **partner-review preview** of the new HeatCrafter site (fireplace showroom, Buffalo Grove IL, North Shore service area). It is a static site deployed by GitHub Pages. Art Kalina (`artiomk`) is the owner and final decision-maker.

## Roles (agreed 2026-11-12)

| Collaborator | Primary ownership |
|---|---|
| **Art** | Business decisions, publishing (runs the local publish script), access grants, final say on copy/pricing/claims/launch |
| **Claude** (Art's Cowork session) | Pencil design files, visual design, page layouts, design exports, the injected script/style layers, design consistency, responsive work |
| **Codex / ChatGPT** | Technical development, repo maintenance, functional testing, navigation verification, source auditing, SEO/technical review, cross-page validation, independent QA |
| **Charlie** (planned — NOT yet invited) | Product information only: products, specs, pricing, images, availability. Blocked on the product-data architecture proposal; no access yet |

Either agent may propose improvements anywhere; implementation respects the source-of-truth rules below. Disagreements go to Art.

## Deployment

- Push to `main` → GitHub Pages redeploys automatically in ~1 minute.
- Live URL: **https://fullyeqpd.github.io/heatcrafter/** (lowercase path; the repo-cased path 404s).
- `heatcrafter.com` is NOT pointed here yet. Do not configure a custom domain, and do not remove the `noindex` meta tags — both happen only at go-live, on Art's say-so.

## What this site is (important)

Every page was **exported from a Pencil design file** on Art's Mac, then post-processed. Consequences:

- Pages live at `/{slug}/index.html` (88 pages). Markup is machine-generated: one big tree of `<div>`s with inline styles and `data-pencil-name` attributes. There is no templating system; the header/footer markup is duplicated into every page.
- **The Pencil design is the source of truth for layout and copy.** If Art changes the design, Claude re-exports affected pages and the generated markup is replaced wholesale. Hand edits inside the generated markup will be lost on the next re-export of that page.
- **Safe places to edit** (these are re-applied by Claude's build and survive re-exports *if you tell Claude about them* — see Coordination):
  - The injected `<script>` blocks at the bottom of each page: nav link-map (`MAP`), header dropdown menus (`DD`), collapsible Q&A accordions (`ANS` — includes answer copy that exists nowhere else), scale-to-fit (`function fit()`).
  - The injected `<style>` blocks in `<head>`: body centering, `hc-dd` dropdown styles, the `[data-pencil-name="Header"]` width fix.
- These injected blocks are **duplicated in all 88 pages**. Any change to them must be applied to every page (script it — don't hand-edit 88 files).

## Known quirks

- No real `<a>` links exist in the generated markup; navigation is synthesized by the `MAP` click-script from visible label text. If a label is renamed in the design, its link silently dies — worth checking after content changes.
- Pages are fixed 1440px wide. Phones get `<meta name="viewport" content="width=1440">`; smaller desktop windows get `body{zoom}` from the fit script. Don't add `width=device-width` back.
- `images/` is ~200MB of PNGs referenced by depth-relative paths (`../../images/...`). Don't rename images; several pages share them.
- The 20 collapsed-question answers in the `ANS` map were written by Claude in Aug 2026 and are pending Art's final copy review.

## Coordination rules

1. **Pull before you push. Never force-push.** Claude's updates arrive as ordinary commits on `main` (via a script Art runs locally); force-pushing destroys them, and vice versa.
2. Small, safe fixes (typos in injected copy, CSS polish, script bugs): commit directly to `main` with a clear message — the message is how Claude learns what you changed.
3. Larger changes (restructuring, new behavior, anything touching many pages): open a branch + PR and let Art decide.
4. If you want a **content or layout** change inside the generated markup, don't edit it directly — leave the request in a commit message, PR description, or a note in `NOTES-FOR-CLAUDE.md` (create it if needed) so Claude changes it in the Pencil design / build layer instead. Claude reads this repo's history before every rebuild and will fold your injected-layer changes into the build so re-exports don't clobber them.
5. Review findings that aren't code (copy inconsistencies, UX issues, broken flows) → write them to `REVIEW-FINDINGS.md` at the repo root, newest on top, so Art and Claude see one running list.

## Good first review targets

- Click every nav label and dropdown item; the link-map is text-matched and fragile.
- Brand/product naming consistency (Stûv vs Stuv vs Stuv6 was a known issue in the old site).
- The 20 authored Q&A answers (`ANS` map) for factual tone and accuracy.
- Lighthouse/page-weight: pages are 200–600KB of HTML each plus heavy PNGs; compression suggestions welcome — but keep changes in the safe layers.
