# HeatCrafter Preview Site — Agent Guide

This repo is the **partner-review preview** of the new HeatCrafter site (fireplace showroom, Buffalo Grove IL, North Shore service area). It is a static site deployed by GitHub Pages. Art Kalina (`artiomk`) is the owner and final decision-maker.

## Roles (agreed 2026-11-12)

| Collaborator | Primary ownership |
|---|---|
| **Art** | Business decisions, access grants, final say on copy/pricing/claims/launch |
| **Claude** (Art's Cowork session) | Shared ownership with Codex: Pencil designs, visual design, page layouts, responsive work, design exports, implementation, publishing through the established workflow, and QA |
| **Codex / ChatGPT** | Shared ownership with Claude: Pencil designs, visual design, page layouts, responsive work, design exports, implementation, publishing through the established workflow, and QA; also repo maintenance, SEO/technical review, and cross-page validation |
| **Charlie** (planned — NOT yet invited) | Product information only: products, specs, pricing, images, availability. Blocked on the product-data architecture proposal; no access yet |

Art explicitly authorized Codex to work directly in Pencil alongside Claude and to make visual, design, responsive, and implementation changes both during preview and after the website goes live. This supersedes the earlier Claude-only design ownership: Codex does not need to route design work through Claude or ask again solely because a task is visual. Both agents follow the source-of-truth and coordination rules below. Disagreements go to Art.

## Deployment

- Push to `main` → GitHub Pages redeploys automatically in ~1 minute.
- Live URL: **https://fullyeqpd.github.io/heatcrafter/** (lowercase path; the repo-cased path 404s).
- `heatcrafter.com` is NOT pointed here yet. Do not configure a custom domain, and do not remove the `noindex` meta tags — both happen only at go-live, on Art's say-so.

## What this site is (important)

Every page was **exported from a Pencil design file** on Art's Mac, then post-processed. Consequences:

- Pages live at `/{slug}/index.html` (89 pages). Markup is machine-generated: one big tree of `<div>`s with inline styles and `data-pencil-name` attributes. There is no templating system; the header/footer markup is duplicated into every page.
- **The Pencil design is the source of truth for layout and copy.** When either agent changes the design, that agent re-exports affected pages and the generated markup is replaced wholesale. Hand edits inside the generated markup will be lost on the next re-export of that page.
- The responsive layer is shared source in `assets/responsive.css` and `assets/responsive.js`; `tools/apply-responsive.py` reapplies classes and navigation to the exports. The new company page body is maintained in `templates/about-chimney-monkey.html` and mirrored in Pen. Keep both in sync when changing that page.
- **Safe places to edit** (these are re-applied by Claude's build and survive re-exports *if the changes are recorded for the other agent* — see Coordination):
  - The injected `<script>` blocks at the bottom of each page: nav link-map (`MAP`), header dropdown menus (`DD`), collapsible Q&A accordions (`ANS` — includes answer copy that exists nowhere else), scale-to-fit (`function fit()`).
  - The injected `<style>` blocks in `<head>`: body centering, `hc-dd` dropdown styles, the `[data-pencil-name="Header"]` width fix.
- These injected blocks are **duplicated in all exported pages**. Any change to them must be applied to every page (script it — don't hand-edit 88 files).
- After every Pencil export/overlay, run `python3 tools/prepare-site.py` and `python3 tools/check-site.py`. This preserves the responsive layer, the sister-company page, both external partner links, and the internal About Chimney Monkey footer link. See `NOTES-FOR-CLAUDE.md`.

## Known quirks

- Most navigation is synthesized by the `MAP` click-script from visible label text; the footer partner names are semantic `<a>` links added by the post-export helper. If a navigation label is renamed in the design, its link silently dies — worth checking after content changes.
- The desktop Pencil canvas remains 1440px wide. Below 1400px, shared `assets/responsive.css` reflows the page at normal scale with a device-width viewport; phones stack content and tablets use two-column grids and a touch menu. At 1400px and wider, desktop scaling preserves the edge-to-edge presentation. `tools/apply-preview-fit.py` now delegates to the responsive helper so older publishing instructions cannot restore phone scaling.
- `images/` is ~200MB of PNGs referenced by depth-relative paths (`../../images/...`). Don't rename images; several pages share them.
- The 20 collapsed-question answers in the `ANS` map were written by Claude in Aug 2026 and are pending Art's final copy review.

## Coordination rules

1. **Pull before you push. Never force-push.** Claude's updates arrive as ordinary commits on `main` (via a script Art runs locally); force-pushing destroys them, and vice versa.
2. Small, safe fixes (typos in injected copy, CSS polish, script bugs): commit directly to `main` with a clear message — the message is how Claude learns what you changed.
3. Use a branch + PR for larger changes so the scope and diff stay reviewable. Art's standing approval (2026-11-12) covers implementing, checking, merging, and publishing routine design and technical changes within the requested task, including changes repeated across many pages; do not ask again solely because a PR or deployment is involved. Complete the necessary checks and respect enforced repository protections. Ask only when a material new decision or expanded scope is needed, or a platform requires confirmation at action time.
4. Either agent may implement **content or layout** changes directly in the Pencil design / build layer and re-export affected pages. Avoid standalone edits inside generated markup that would be lost on re-export. Both agents read the latest repo history and coordination notes before rebuilding, incorporate recorded injected-layer changes into the build, and document which design pages and files changed.
5. Review findings that aren't code (copy inconsistencies, UX issues, broken flows) → write them to `REVIEW-FINDINGS.md` at the repo root, newest on top, so Art and both agents see one running list.
6. For simultaneous work, record the pages/components and files each agent is editing before making changes. Work on separate pages or branches where possible; serialize edits to the same Pencil document or shared components unless the editor provides verified conflict-safe collaboration. Confirm the active Pencil file before editing, re-read shared state before export, and preserve the other agent's changes.
7. This authorization continues after launch. Use the established publishing workflow and the standing approval in rule 3. Initial production cutover, domain changes, and removal of `noindex` remain explicit launch decisions.

## Communication preference (Art, 2026-11-12)

- Always suggest concrete next steps at handoff under **NEXT STEPS**.
- Clearly label anything Art needs to do with **YOUR ACTION**. If no action is needed, say so when relevant. Use uppercase labels and concise, plain-language instructions.

## Good first review targets

- Click every nav label and dropdown item; the link-map is text-matched and fragile.
- Brand/product naming consistency (Stûv vs Stuv vs Stuv6 was a known issue in the old site).
- The 20 authored Q&A answers (`ANS` map) for factual tone and accuracy.
- Lighthouse/page-weight: pages are 200–600KB of HTML each plus heavy PNGs; compression suggestions welcome — but keep changes in the safe layers.
