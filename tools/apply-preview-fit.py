#!/usr/bin/env python3
"""Reapply full-width preview scaling after a Pencil HTML export."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OLD = "document.body.style.zoom=(w<1440)?(w/1440):'';"
NEW = "document.body.style.zoom=w/1440;"


def main():
    pages = sorted(ROOT.rglob("index.html"))
    updates = []
    for path in pages:
        html = path.read_text()
        if 'data-pencil-name="Page/' not in html:
            continue
        if html.count(OLD) + html.count(NEW) != 1:
            raise SystemExit(f"Expected one known preview-fit script: {path.relative_to(ROOT)}")
        if OLD in html:
            updates.append((path, html.replace(OLD, NEW)))
    for path, html in updates:
        path.write_text(html)
    print(f"Updated {len(updates)} pages; checked {len(pages)} index pages.")


if __name__ == "__main__":
    main()
