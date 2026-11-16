# HeatCrafter Preview Site — Agent Guide

This repo is the **partner-review preview** of the new HeatCrafter site (fireplace showroom, Buffalo Grove IL, North Shore service area). It is a static site deployed by GitHub Pages. Art Kalina (`artiomk`) is the owner and final decision-maker.

## Team (updated 2026-11-16, per Art)

| Collaborator | Role |
|---|---|
| **Art Kalina** (`artiomk`) | Owner & final decision-maker: business strategy, final approvals, publishing decisions, team access |
| **Ember** (Claude · info@heatcrafter.com) | Website development collaborator — equal partner with Codex |
| **Codex** (ChatGPT) | Website development collaborator — equal partner with Ember |
| **Charlie Dreiske** (`CharlieDreiske` · Claude: charlie@chimneymonkey.com) | Product catalog manager — product information only, restricted workflow (access being set up; no write access yet) |

**Ember and Codex are equal and interchangeable.** Both are authorized to work across the entire HeatCrafter website: design, layouts, and UX; Pencil design files and generated pages; frontend development and functionality; navigation, menus, and interactive features; SEO/GEO and content optimization; product catalog architecture and integration; technical maintenance and performance; testing, troubleshooting, and QA; GitHub repository maintenance and deployment; website content and page development.

Neither agent has exclusive ownership of design or code. Either should be able to continue, improve, fix, or complete work started by the other, and either may independently audit or verify the other's work. If one agent becomes unavailable or hits usage limits, the other continues without rebuilding the project — keep shared documentation sufficient for that at all times. Disagreements go to Art.

## Collaboration rules

1. **GitHub is the shared source of truth.**
2. Read `AGENTS.md`, recent commits, `REVIEW-FINDINGS.md`, and the relay notes (`NOTES-FOR-CLAUDE.md`, `NOTES-FOR-CODEX.md`) before starting work.
3. Pull the latest changes before making modifications.
4. **Never force-push** or overwrite another collaborator's work.
5. Maintain the Pencil design source and export process so changes survive regeneration (see "Design-source dependency" below).
6. Document significant changes and decisions — in commit messages, `REVIEW-FINDINGS.md`, or the relay notes.
7. Use clear commit messages so the other agent understands what changed.
8. Help resolve issues discovered by the other agent.
9. Either agent may independently audit or verify the other's work.
10. If one agent is unavailable, the other continues from the repo + documentation alone.

Shared capability does not mean simultaneous editing of the same files: record the pages/components you are actively editing (relay notes or commit messages), work on separate pages or branches where possible, and serialize edits to the same Pencil document or shared components. Art's standing approval (2026-11-12) covers implementing, checking, merging, and publishing routine design and technical changes within a requested task, including changes repeated across many pages; ask only when a material new decision or expanded scope is needed.

## Single-collaborator dependencies (keep this register current)

Per Art: the export pipeline must not create permanent ownership boundaries. Where a workflow depends on something only one collaborator can reach, it is listed here with the continuation path for the other:

| Dependency | Who has it | How the other continues |
|---|---|---|
| Pencil design files (`.pen`, on Art's Mac) + export | Ember (via Art's desktop session) | Generated pages in this repo are the canonical runtime. If Ember is unavailable, Codex may edit generated markup directly for needed changes, **logging each such edit in `NOTES-FOR-CLAUDE.md`** so the design source is reconciled before the next re-export (unlogged hand edits get clobbered). Design-source change requests go in the relay notes. |
| Mac publish script (`update-site.sh`) + 200MB images folder | Art runs it; Ember maintains it | Only needed for full re-exports and new images. Individual page/file commits work through normal git/GitHub for both agents. New images can be added by committing them under `images/` directly. |
| Shared responsive/nav layer rebuild | Either agent | `python3 tools/prepare-site.py` + `python3 tools/check-site.py` from repo root — in-repo, runnable by anyone, idempotent. Run after every export/overlay. |
| Ember↔Codex messaging | Both | `NOTES-FOR-CLAUDE.md` (Codex→Ember), `NOTES-FOR-CODEX.md` (Ember→Codex), `REVIEW-FINDINGS.md` (QA log, newest on top). |

## Charlie — product catalog scope

Charlie manages **product information only**: adding products; descriptions and specifications; images, features, finishes, and options; brands, model information, pricing, and availability. He must not be able to independently modify global design, navigation, templates, unrelated pages, or deployment settings.

GitHub cannot enforce folder-level write restrictions inside one repo, so Charlie's workflow will be a separate structured product-data channel (products repo / catalog files) whose changes Ember or Codex integrate into the site; he gets no direct write access to this repo. Until that workflow is set up and approved by Art, Charlie has no access.

## Deployment

- Push to `main` → GitHub Pages redeploys automatically in ~1 minute.
- Live URL: **https://fullyeqpd.github.io/heatcrafter/** (lowercase path; the repo-cased path 404s).
- `heatcrafter.com` is NOT pointed here yet.

**Safeguards (unchanged, apply to everyone):** no force-pushing; no production-domain changes without Art's approval; no removal of the `noindex` meta tags before launch; no major unapproved changes to the website.

## What this site is (important)

Every page was **exported from a Pencil design file** on Art's Mac, then post-processed. Consequences:

- Pages live at `/{slug}/index.html` (89 pages). Markup is machine-generated: one big tree of `<div>`s with inline styles and `data-pencil-name` attributes. There is no templating system; the header/footer markup is duplicated into every page.
- **The Pencil design is the source of truth for layout and copy.** When the design changes, affected pages are re-exported and the generated markup is replaced wholesale. Hand edits inside the generated markup are lost on the next re-export of that page unless logged for reconciliation (see dependency register).
- The responsive layer is shared source in `assets/responsive.css` and `assets/responsive.js`; `tools/apply-responsive.py` reapplies classes and navigation to the exports. The company page body is maintained in `templates/about-chimney-monkey.html` and mirrored in Pen. Keep both in sync when changing that page.
- **Safe places to edit** (re-applied by the build and surviving re-exports *if recorded for the other agent*):
  - The injected `<script>` blocks at the bottom of each page: nav link-map (`MAP`), header dropdown menus (`DD`), collapsible Q&A accordions (`ANS` — includes answer copy that exists nowhere else), scale-to-fit (`function fit()`).
  - The injected `<style>` blocks in `<head>`: body centering, `hc-dd` dropdown styles, the `[data-pencil-name="Header"]` width fix.
- These injected blocks are **duplicated in all exported pages**. Any change to them must be applied to every page (script it — don't hand-edit 88 files).
- After every Pencil export/overlay, run `python3 tools/prepare-site.py` and `python3 tools/check-site.py`. This preserves the responsive layer, the sister-company page, both external partner links, and the internal About Chimney Monkey footer link. See `NOTES-FOR-CLAUDE.md`.
- Known Pencil-side debts (changes made in generated pages, not yet mirrored in the design source — re-exports of these pages regress without reconciliation): cart-CTA/shipping copy removals; the 20 formerly-overlapping canvas frames; /about/ Google Maps embeds (2026-11-16); /about/ owner section de-personalized to team voice (2026-11-16).

## Known quirks

- Most navigation is synthesized by the `MAP` click-script from visible label text; the footer partner names are semantic `<a>` links added by the post-export helper. If a navigation label is renamed in the design, its link silently dies — worth checking after content changes.
- The desktop Pencil canvas remains 1440px wide. Below 1400px, shared `assets/responsive.css` reflows the page at normal scale with a device-width viewport; phones stack content and tablets use two-column grids and a touch menu. At 1400px and wider, desktop scaling preserves the edge-to-edge presentation. `tools/apply-preview-fit.py` now delegates to the responsive helper so older publishing instructions cannot restore phone scaling.
- `images/` is ~200MB of PNGs referenced by depth-relative paths (`../../images/...`). Don't rename images; several pages share them.
- The 20 collapsed-question answers in the `ANS` map were written by Ember in Aug 2026 and are pending Art's final copy review.

## Communication preference (Art, 2026-11-12)

- Always suggest concrete next steps at handoff under **NEXT STEPS**.
- Clearly label anything Art needs to do with **YOUR ACTION**. If no action is needed, say so when relevant. Use uppercase labels and concise, plain-language instructions.

## Good review targets

- Click every nav label and dropdown item; the link-map is text-matched and fragile.
- Brand/product naming consistency (Stûv vs Stuv vs Stuv6 was a known issue in the old site).
- The 20 authored Q&A answers (`ANS` map) for factual tone and accuracy.
- Lighthouse/page-weight: pages are 200–600KB of HTML each plus heavy PNGs; compression suggestions welcome — but keep changes in the safe layers.
