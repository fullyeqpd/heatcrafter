#!/usr/bin/env python3
"""Apply the heatcrafter-products catalog to the generated site pages.

Patches ONLY plain-text price values at known data-pencil-name anchors:
  - each product's detail page: `price` (display) and `pricenote` (note)
  - every page: `CardPrice` of a product card whose `CardName` matches the product
Never touches markup, styles, images, copy, or any other field. Idempotent.

Usage: python3 tools/apply-catalog.py --catalog ../catalog [--check]
  --check  report drift but change nothing (exit 1 if drift found)

display_status / active / specs are NOT applied automatically (site-team review
required for those); `active: false` and status changes are reported only.
"""
import argparse, glob, json, os, re, sys

# Distinctive, word-bounded match patterns for product cards (CardName variants).
CARD_MATCH = {
    "enviro-g39": r"\bG39\b",
    "enviro-ex35": r"\bEX35\b",
    "enviro-e33": r"\bE33\b",
    "enviro-q1": r"\bQ1\b",
    "enviro-ri30": r"\bRi30\b",
    "kozy-heat-chaska-29": r"\bChaska 29\b",
    "empire-blackburn-36": r"\bBlackburn 36\b",
    "modern-flames-redstone": r"\bRedstone\b",
    "dimplex-optimyst-aura": r"\bOptimyst\b",
    "stuv-6": r"Stûv ?6(?!\d)",
    "stuv-16": r"Stûv ?16\b",
    "real-fyre-chestnut-oak": r"\bChestnut Oak\b",
    "real-fyre-coastal-driftwood": r"\bCoastal Driftwood\b",
    "real-fyre-rugged-forest-split": r"\bRugged Forest\b",
    "real-fyre-split-oak-designer-plus": r"\bSplit Oak Designer\b",
    "grand-canyon-lava-burner-glowfire": r"\bLava Burner\b",
    "grand-canyon-aspen-birch": r"\bAspen Birch\b",
    "grand-canyon-red-oak": r"\bRed Oak\b",
    "grand-canyon-weathered-oak": r"\bWeathered Oak\b",
    "superior-traditional-with-enclosure": r"\bSuperior Traditional\b",
    "farmhouse-non-combustible": r"\bFarmhouse\b",
}

TEXT_RE = r'(class="hc-text[^"]*">)(\s*)([^<]*?)(\s*)(</div>)'

def set_anchor_text(html, anchor, new_text, start=0, window=None):
    """Replace the first hc-text content after data-pencil-name=anchor. Returns (html, old or None)."""
    m = re.search('data-pencil-name="%s"' % anchor, html[start:window and start + window or len(html)])
    if not m:
        return html, None
    pos = start + m.start()
    m2 = re.compile(TEXT_RE).search(html, pos)
    if not m2 or m2.start() - pos > 2000:
        return html, None
    old = re.sub(r"\s+", " ", m2.group(3)).strip()
    if old == new_text or old.startswith(new_text + " ·"):
        return html, new_text  # already canonical (suffixed copy is preserved)
    new = m2.group(1) + m2.group(2) + new_text + m2.group(4) + m2.group(5)
    return html[:m2.start()] + new + html[m2.end():], old

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True, help="path to heatcrafter-products checkout")
    ap.add_argument("--site", default=".", help="site repo root")
    ap.add_argument("--check", action="store_true", help="report drift, change nothing")
    args = ap.parse_args()

    products = {}
    for f in sorted(glob.glob(os.path.join(args.catalog, "products", "*.json"))):
        p = json.load(open(f))
        products[p["id"]] = p
    if not products:
        sys.exit("no products found in catalog")

    changed_files, drift, errors, notes = set(), [], [], []

    # 1. Detail pages
    for pid, p in products.items():
        if not p.get("site_page"):
            continue
        page = os.path.join(args.site, p["site_page"], "index.html")
        if not os.path.exists(page):
            errors.append(f"{pid}: site_page {p['site_page']} missing on disk")
            continue
        html = orig = open(page).read()
        html, old = set_anchor_text(html, "price", p["price"]["display"])
        if old is None:
            errors.append(f"{pid}: no `price` anchor on {p['site_page']}")
        elif old != p["price"]["display"]:
            drift.append(f"{p['site_page']}: price {old!r} -> {p['price']['display']!r}")
        if p["price"].get("note"):
            html, old = set_anchor_text(html, "pricenote", p["price"]["note"])
            if old is not None and old != p["price"]["note"]:
                drift.append(f"{p['site_page']}: note {old!r} -> {p['price']['note']!r}")
        if html != orig and not args.check:
            open(page, "w").write(html)
            changed_files.add(page)
        if not p.get("active", True):
            notes.append(f"{pid}: active=false — page removal needs site-team action")

    # 2. Product cards on all pages
    pages = glob.glob(os.path.join(args.site, "**", "index.html"), recursive=True)
    for page in pages:
        html = orig = open(page).read()
        for m in re.finditer('data-pencil-name="CardName"', html):
            seg = html[m.start():m.start() + 1200]
            t = re.search(TEXT_RE, seg)
            name = re.sub(r"\s+", " ", t.group(3)).strip() if t else ""
            hit = next((pid for pid, pat in CARD_MATCH.items()
                        if pid in products and re.search(pat, name)), None)
            if not hit:
                continue
            new_html, old = set_anchor_text(html, "CardPrice", products[hit]["price"]["display"],
                                            start=m.start(), window=6000)
            if old is not None and old != products[hit]["price"]["display"]:
                drift.append(f"{os.path.relpath(page, args.site)}: card {name!r} {old!r} -> {products[hit]['price']['display']!r}")
            html = new_html
        if html != orig and not args.check:
            open(page, "w").write(html)
            changed_files.add(page)

    for n in notes: print("NOTE:", n)
    for d in drift: print("DRIFT:" if args.check else "PATCHED:", d)
    for e in errors: print("ERROR:", e)
    print(f"{len(products)} products; {len(drift)} price value(s) "
          f"{'drifting' if args.check else 'patched'}; {len(changed_files)} file(s) "
          f"{'would change' if args.check else 'changed'}; {len(errors)} error(s)")
    if errors or (args.check and drift):
        sys.exit(1)

if __name__ == "__main__":
    main()
