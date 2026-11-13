#!/usr/bin/env python3
"""Check export integrity, local links, and responsive entry points."""
from pathlib import Path
import re
from export_markup import ExportMarkup
ROOT=Path(__file__).resolve().parents[1]
pages=list(ROOT.rglob('index.html'))
for path in pages:
    text=path.read_text()
    if 'data-pencil-name="Page/' not in text:continue
    assert text.count('width=device-width')==1,path
    assert text.count('id="hc-mobile-nav"')==1,path
    assert text.count('class="hc-sister-footer"')==1,path
    assert 'document.body.style.zoom=w>=1400?w/1440:1;' in text,path
    assert 'noindex, nofollow' in text,path
    for n in ExportMarkup(text).nodes:
        if n['tag'] not in ('a','link','script','img'):continue
        attr='src' if n['tag'] in ('script','img') else 'href'
        url=n['attrs'].get(attr,'')
        if not url or re.match(r'(?:https?:|mailto:|tel:|#|data:)',url):continue
        target=(path.parent/url.split('#')[0].split('?')[0]).resolve()
        assert target.exists(),f'{path.relative_to(ROOT)}: missing {url}'
assert 'class="hc-sister-page"' in (ROOT/'about-chimney-monkey/index.html').read_text()
print(f'Checked {len(pages)} pages: responsive entry points, sister links, local targets/assets, and noindex preserved.')
