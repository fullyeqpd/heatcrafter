# Responsive layout release checks — 2026-11-12

Scope: all 88 existing pages plus `/about-chimney-monkey/`.

## Browser checks

- Chrome browser viewport checks at 320, 390, 820, 1024, 1366, and 1512px: 534 page/width combinations, zero document overflow or overflowing text boxes.
- After final company-page and comparison-table refinements, repeated the affected eight pages at all six widths: 48 additional checks, zero failures.
- Visual inspection: phone homepage/room cards, iPad product detail, phone sister-company page, and final desktop/tablet previews. These are browser viewport checks, not physical iPad/iPhone hardware tests.
- Mobile menu opens and closes, expandable Fireplaces links navigate to the category, and Escape closes the menu and restores focus to the button.
- About Chimney Monkey in the footer opens the internal sister-company page; original partner-name links still point directly to `https://chimneymonkey.com/`.
- Comparison and cost tables keep columns aligned instead of losing the association between headings and values on phones.

## Source checks

- `python3 tools/check-site.py`: unique viewport/menu/footer link, correct local routes/assets, responsive fit behavior, and noindex on all 89 pages.
- `python3 tools/prepare-site.py`: a second complete run yields identical final page hashes; each helper may rewrite intermediate markup during the rebuild, but the resulting site is identical.
- Reversing only the responsive annotations, navigation additions, viewport, and fit-script replacement restores all 88 original HTML files byte-for-byte. Existing text, assets, prices, and original scripts are preserved.
- `node --check assets/responsive.js` and `git diff --check` pass.

## Shared design and release limits

- Pen includes the new company page, Footer link, and phone/iPad hero references. Existing desktop canvases remain the design source; shared code handles reflow.
- No custom-domain cutover or noindex removal. Existing preview-only forms, placeholder reviews, and unresolved product-copy questions remain outside this layout release.
- The deploy must be verified after merge; add the release receipt to the repository log.
