#!/usr/bin/env python3
"""Apply the shared responsive layer after Pencil exports. Safe to rerun."""
from pathlib import Path
import re, json, hashlib, html as escape
from export_markup import ExportMarkup, replace_ranges
ROOT=Path(__file__).resolve().parents[1]
CSS_VERSION=hashlib.sha256((ROOT/'assets/responsive.css').read_bytes()).hexdigest()[:10]
JS_VERSION=hashlib.sha256((ROOT/'assets/responsive.js').read_bytes()).hexdigest()[:10]

def px(value):
    try:return float(value.removesuffix('px'))
    except (ValueError,AttributeError):return 0

def classify(n):
    s=n['style']; name=n['name']; children=n['children']; classes=[]
    if not name:return classes
    if name.startswith('Page/'):return ['hc-page']
    if n['tag']=='svg':return []
    if n['parent'] and n['parent']['name'].startswith('Page/') and name not in ('Header','Footer'):classes+=['hc-section']
    if 'font-size' in s:
        size=px(s['font-size']);classes+=['hc-text']
        if size>=48:classes+=['hc-display']
        elif size>=32:classes+=['hc-heading']
        elif size>=22:classes+=['hc-subheading']
        elif size>=14:classes+=['hc-copy']
    if s.get('display')=='flex':
        classes+=['hc-flex']
        if s.get('flex-direction')=='row':
            substantial=[c for c in children if px(c['style'].get('width'))>=180 or c['style'].get('flex')=='1 1 0']
            if len(substantial)>=2:classes+=['hc-columns']
            else:classes+=['hc-wrap']
        else:classes+=['hc-column']
    if px(s.get('width'))>=180 or s.get('width')=='100%' or s.get('flex')=='1 1 0':classes+=['hc-fluid']
    if 'url(' in s.get('background-image','') and s.get('position')!='absolute' and px(s.get('height'))>=140 and px(s.get('width'))>=180:classes+=['hc-photo']
    if s.get('position')=='relative' and not s.get('display') and name not in ('Section/Hero','Section/RoomHero'):classes+=['hc-artwork']
    return classes

def link(label,slug,prefix,cls=''):
    href=prefix+slug.strip('/')+'/' if slug!='/' else prefix or './'
    return f'<a class="{cls}" href="{href}">{escape.escape(label)}</a>'

def apply(path):
    original=path.read_text(); content=original
    if 'data-pencil-name="Page/' not in content:return False
    content=re.sub(r'<!-- hc-responsive-menu -->.*?<!-- /hc-responsive-menu -->','',content,flags=re.S)
    content=re.sub(r'<button class="hc-menu-toggle".*?</button>','',content,flags=re.S)
    content=re.sub(r'<a class="hc-sister-footer".*?</a>','',content,flags=re.S)
    content=re.sub(r'<link data-hc-responsive[^>]*>\n?','',content)
    content=re.sub(r'<script data-hc-responsive[^>]*></script>\n?','',content)
    content=re.sub(r' class="hc-(?:[^"]*)"', lambda m: m.group(0) if m.group(0) == ' class="hc-sister-page"' else '', content)
    prefix='../'*len(path.relative_to(ROOT).parts[:-1])
    content=content.replace('w>=1200?w/1440:1','w>=1400?w/1440:1')
    content=content.replace('content="width=1440"','content="width=device-width, initial-scale=1"')
    content=content.replace('document.body.style.zoom=w/1440;', 'document.body.style.zoom=w>=1400?w/1440:1;')
    content=content.replace("document.body.style.zoom=(w<1440)?(w/1440):'';",'document.body.style.zoom=w>=1400?w/1440:1;')
    content=re.sub(r'<div\s+data-pencil-name="AboutChimneyMonkey"[^>]*>.*?</div>', '', content, flags=re.S)
    p=ExportMarkup(content);edits=[]
    for n in p.nodes:
        classes=classify(n)
        if classes:edits.append((n['open_end']-1,n['open_end']-1,' class="'+' '.join(classes)+'"'))
    header=p.named('Header'); company=p.named('Col-COMPANY')
    about=next(c for c in company['children'] if 'About HeatCrafter' in p.markup(c))
    edits.append((about['end'],about['end'],link('About Chimney Monkey','/about-chimney-monkey',prefix,'hc-sister-footer')))
    edits.append((header['close_start'],header['close_start'],'<button class="hc-menu-toggle" type="button" aria-expanded="false" aria-controls="hc-mobile-nav">Menu <span aria-hidden="true">☰</span></button>'))
    dd=json.loads(re.search(r'var DD=(\{.*?\});var PREFIX=',content,re.S).group(1))
    nav=['<!-- hc-responsive-menu --><nav id="hc-mobile-nav" class="hc-mobile-nav" aria-label="Main navigation" hidden>']
    nav.append(link('Book a showroom visit','/schedule-a-visit',prefix,'hc-nav-book'))
    for title,group in dd.items():
        nav.append('<details><summary>'+escape.escape(title)+'</summary><div class="hc-menu-links">')
        for section in group['sections']:
            for label,slug in section[1]:nav.append(link(label,slug,prefix))
        nav.append(link(*group['footer'],prefix))
        nav.append('</div></details>')
    for label,slug in [('Installation','/installation'),('About HeatCrafter','/about'),('About Chimney Monkey','/about-chimney-monkey'),('Contact','/contact')]:nav.append(link(label,slug,prefix))
    nav.append('</nav><!-- /hc-responsive-menu -->')
    edits.append((header['end'],header['end'],''.join(nav)))
    content=replace_ranges(content,edits)
    content=content.replace('</head>',f'<link data-hc-responsive rel="stylesheet" href="{prefix}assets/responsive.css?v={CSS_VERSION}" />\n</head>')
    content=content.replace('</body>',f'<script data-hc-responsive src="{prefix}assets/responsive.js?v={JS_VERSION}"></script>\n</body>')
    if content!=original:path.write_text(content);return True
    return False

if __name__=='__main__':
    pages=list(ROOT.rglob('index.html')); count=sum(apply(path) for path in pages)
    print(f'Updated {count} of {len(pages)} pages.')
