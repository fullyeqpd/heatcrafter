# HeatCrafter shared implementation notes

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
