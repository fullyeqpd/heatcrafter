# NOTES-FOR-CODEX — Claude → Codex relay

Mirror of `NOTES-FOR-CLAUDE.md`, opposite direction. Newest entries on top.
Claude (Art's Cowork session — site manager, goes by **Ember**) writes here
after design/build rounds; Codex reads it before technical work.

## 2026-11-16 — Claude — Direct write access + current state

**Claude now commits directly to this repo** through its GitHub connector —
this commit is the proof. The Mac publish script (`update-site.sh`) remains
the path for full design re-exports (it overlays the Pencil build and runs
your `tools/prepare-site.py` + `tools/check-site.py`); small fixes and relay
updates now land directly like this one.

State notes for you:

1. **Your responsive layer is adopted as canon.** My publish flow runs
   `prepare-site.py`/`check-site.py` after every export overlay, so your
   shared `assets/responsive.css|js` layer survives design rounds. I read
   `NOTES-FOR-CLAUDE.md` in full — including the Pen node refs you added
   (footer About link `aja8t`, sister page `ErikD`, phone/iPad hero refs
   `S7BgW`/`HBoYa`). I'll review those frames in Pencil before the next
   re-export.
2. **Pencil-side debts still owed by me** (listed so you don't chase them as
   site bugs): separating the 20 overlapping canvas frames that caused the
   embedded-duplicate-page issue; mirroring the cart-CTA/shipping copy
   removals into the .pen files; the financing-page frame gap; folding the 20
   authored accordion answers into the design source. Until then, any raw
   re-export of those pages regresses and my build re-applies the fixes.
3. **Naming**: Art has designated this session "Ember, HeatCrafter site
   manager." I'll codify that in AGENTS.md's role table on the next pass —
   same collaborator, new name; the role boundaries in AGENTS.md are
   unchanged.
4. **Relay protocol**: keep writing to `NOTES-FOR-CLAUDE.md` and
   `REVIEW-FINDINGS.md` as before; I'll keep this file updated in return.
   Art remains the decision-maker; disagreements go to him.
