# HeatCrafter shared implementation notes

## 2026-11-12 — Codex — Header flame animation

The header logo uses a small decorative SVG overlay in `assets/responsive.js`
and `assets/responsive.css`. The original PNG and Pen artwork are unchanged.
The flame, warm halo, and rays animate for 3.6 seconds on load, then settle;
mouse hover or keyboard focus replays the effect. There is no perpetual loop.
Reduced-motion users receive a still amber flame. The bear and lettering do
not animate. Header mark dimensions are 40×45px (36×41px on phones).

The combined export helper preserves this behavior. CSS/JS references now
include content hashes, so a release updates cached shared assets reliably.
No Pen re-export is required for this runtime-only effect.


## 2026-11-12 — Codex — Responsive layouts and sister-company page

Art authorized proper iPad/mobile layouts and an About Chimney Monkey page
explaining the sister-company relationship. The shared responsive layer now
covers all 89 pages, with a 1400px breakpoint (including iPad Pro landscape).
Phone layouts stack content; tablet layouts use two-column grids. Navigation
uses a native button, expandable groups, ordinary links, and Escape dismissal.
Comparison/cost tables retain aligned columns on phones.

After overlaying any Pencil HTML export, run from this repository:

```sh
python3 tools/prepare-site.py
python3 tools/check-site.py
```

`prepare-site.py` rebuilds the sister page with the current exported About
header/footer, reapplies the external partner anchors, and reapplies responsive
classes, viewport, internal sister link, menu, and CSS/JS includes. It is
idempotent. `apply-preview-fit.py` remains as a compatibility entry point and
now delegates to the responsive helper; the older scaling instructions below
are historical and superseded.

Shared source: `assets/responsive.css`, `assets/responsive.js`,
`tools/apply-responsive.py`, and `tools/export_markup.py`. The company-page
body lives in `templates/about-chimney-monkey.html`; update it alongside the
Pen copy if changing that content. Existing exported copy/assets are retained.
No domain, noindex, product, pricing, or form-delivery changes are included.

Pen updates in the main HeatCrafter document:
- Shared Footer: About Chimney Monkey (`aja8t`) in Col-COMPANY.
- Full desktop sister-company page: `ErikD`.
- Phone (390px) and iPad (820px) hero references: `S7BgW` and `HBoYa`.
- Existing desktop pages were not duplicated into 88 device-specific canvases;
  responsive behavior is maintained in the shared implementation layer.

Pen structural checks report no enabled-node layout problems on the new
frames. Canvas screenshot output was unreliable for the offscreen reference
frames; the browser screenshots and checks in `RESPONSIVE-QA.md` are the visual
verification for this release. Review the references in Pen before re-exporting.

## 2026-11-12 — Codex — Footer partner links

Art requested that the footer's Chimney Monkey mention link to
`https://chimneymonkey.com/`. Both occurrences (FTagline and Copyright)
now use ordinary inline anchors around only the partner name. The existing
text color and layout are preserved, with an underline to identify the links.
They work without JavaScript, support keyboard focus, and open in the same tab.

Reapply this navigation behavior after each Pen HTML export/overlay:

```sh
python3 tools/apply-footer-partner-links.py
```

The helper checks every page before writing and is idempotent. Keep it in
the post-export workflow alongside `apply-preview-fit.py`; the Pen text
nodes retain the full sentences and their existing layout.

## 2026-11-12 — Codex — Desktop preview fills the viewport

Art requested removal of the empty side strips on wider desktop windows.
The exported design remains 1440px wide in Pencil. The injected `fit()`
script now scales the complete page to the available viewport width both
above and below 1440px, preserving the design's proportions and alignment.
This is a preview presentation change, not a tablet/mobile redesign.

The change is confined to the post-export script in all 88 index pages;
the Pencil frames, generated layout/copy, assets, navigation, and noindex
settings are unchanged. No canvas edits are required for this adjustment.

After exporting or overlaying a new design build, reapply the adjustment:

```sh
python3 tools/apply-preview-fit.py
```

Run this from the repository before publishing. The helper validates all
target pages before writing, and running it again makes no further edits.
Both agents should preserve this step in future export/build work.
