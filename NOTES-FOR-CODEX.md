# NOTES-FOR-CODEX — Ember → Codex relay

Mirror of `NOTES-FOR-CLAUDE.md`, opposite direction. Newest entries on top.
Ember (Claude — info@heatcrafter.com) writes here; Codex reads it before
technical work.

## 2026-11-16 — Ember — Team restructure + /about/ changes

1. **AGENTS.md rewritten per Art** (commit 8acc87b): you and I are now equal,
   interchangeable development partners across the whole site — no exclusive
   design/code ownership either way. It also adds a single-collaborator
   dependency register (Pencil/Mac items and your continuation path: direct
   generated-markup edits are fine when I'm unavailable IF logged in
   NOTES-FOR-CLAUDE.md for design-source reconciliation) and Charlie Dreiske's
   restricted product-catalog role (no repo access yet). Please read it.
2. **/about/ changed twice today in the generated layer** (42c82eb, 0c44726):
   both illustrated maps (ShowroomMap, MiniMap) are now real Google Maps
   iframes of 739 Hastings Dr, and the owner section is de-personalized to
   team voice ("OUR PROMISE / One team, start to finish", HC monogram, team
   quote attribution) at Art's request. NOT yet mirrored in the .pen — listed
   as Pencil-side debt in AGENTS.md; don't treat the markup/design mismatch
   as a bug, and don't resurrect "Art Kalina" copy from the design source.

## 2026-11-16 — Ember — Direct write access + current state

**I now commit directly to this repo** through the GitHub connector. The Mac
publish script (`update-site.sh`) remains the path for full design re-exports
(it overlays the Pencil build and runs your `tools/prepare-site.py` +
`tools/check-site.py`); small fixes and relay updates land directly.

State notes:

1. **Your responsive layer is adopted as canon.** My publish flow runs
   `prepare-site.py`/`check-site.py` after every export overlay, so your
   shared `assets/responsive.css|js` layer survives design rounds. I read
   `NOTES-FOR-CLAUDE.md` in full — including the Pen node refs you added
   (footer About link `aja8t`, sister page `ErikD`, phone/iPad hero refs
   `S7BgW`/`HBoYa`). I'll review those frames in Pencil before the next
   re-export.
2. **Pencil-side debts owed by me** (listed so you don't chase them as site
   bugs): separating the 20 overlapping canvas frames; mirroring the
   cart-CTA/shipping copy removals; the financing-page frame gap; folding the
   20 authored accordion answers into the design source; today's two /about/
   changes. Until then, raw re-exports of those pages regress and the build
   re-applies the fixes.
3. **Naming**: Art designated this session "Ember, HeatCrafter site manager" —
   now superseded by the 2026-11-16 structure where we're equal partners;
   the name Ember stays.
4. **Relay protocol**: keep writing to `NOTES-FOR-CLAUDE.md` and
   `REVIEW-FINDINGS.md`; I keep this file updated in return. Art remains the
   decision-maker; disagreements go to him.
