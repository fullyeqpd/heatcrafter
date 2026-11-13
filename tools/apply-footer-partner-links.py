#!/usr/bin/env python3
"""Link the partner name in exported footer text, preserving surrounding markup."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PARTNER = re.compile(r"Chimney\s+Monkey")
LINK_OPEN = '<a href="https://chimneymonkey.com/" style="color:inherit;text-decoration:underline;text-underline-offset:2px">'
FOOTER_TEXT = re.compile(
    r'(<div\s+data-pencil-name="(?:FTagline|Copyright)"[^>]*>)(.*?)(</div>)',
    re.DOTALL,
)


def main():
    updates = []
    checked = 0
    for path in sorted(ROOT.rglob("index.html")):
        html = path.read_text()
        if 'data-pencil-name="Page/' not in html:
            continue
        matches = list(FOOTER_TEXT.finditer(html))
        if len(matches) != 2:
            raise SystemExit(f"Expected two footer text blocks: {path.relative_to(ROOT)}")
        for match in matches:
            text = match.group(2)
            if len(PARTNER.findall(text)) != 1 or ('<a ' in text and LINK_OPEN not in text):
                raise SystemExit(f"Unexpected partner markup: {path.relative_to(ROOT)}")
        updated = FOOTER_TEXT.sub(
            lambda m: m.group(1) + (m.group(2) if LINK_OPEN in m.group(2)
                                   else PARTNER.sub(lambda p: LINK_OPEN + p.group(0) + '</a>', m.group(2))) + m.group(3),
            html,
        )
        checked += 1
        if updated != html:
            updates.append((path, updated))
    for path, html in updates:
        path.write_text(html)
    print(f"Updated {len(updates)} pages; checked {checked} page footers.")


if __name__ == "__main__":
    main()
