#!/usr/bin/env python3
"""Build the sister-company page with the current shared exported header/footer."""
from pathlib import Path
import re
from export_markup import ExportMarkup
ROOT=Path(__file__).resolve().parents[1]
source=(ROOT/'about/index.html').read_text()
p=ExportMarkup(source)
header=p.named('Header');footer=p.named('Footer')
content=source[:header['end']]+'\n'+(ROOT/'templates/about-chimney-monkey.html').read_text()+'\n'+source[footer['start']:]
content=content.replace('Page/About — /about','Page/Chimney Monkey — /about-chimney-monkey')
content=re.sub(r'<title>.*?</title>','<title>About Chimney Monkey — Our Sister Company | HeatCrafter</title>',content)
content=content.replace('</head>','<meta name="description" content="HeatCrafter and Chimney Monkey are sister companies: showroom guidance, fireplace installation, and ongoing chimney service on Chicago’s North Shore." />\n</head>')
# The source menu is between the header and content and is intentionally regenerated.
out=ROOT/'about-chimney-monkey/index.html';out.parent.mkdir(exist_ok=True);out.write_text(content)
print('Built about-chimney-monkey/index.html')
