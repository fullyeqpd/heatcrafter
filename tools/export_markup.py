"""Read exported HTML without reformatting the original document."""
from html.parser import HTMLParser

VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class ExportMarkup(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=False)
        self.html = html
        self.lines = [0]
        for line in html.splitlines(keepends=True): self.lines.append(self.lines[-1] + len(line))
        self.nodes, self.stack = [], []
        self.feed(html)
    def source_offset(self):
        line, col = self.getpos()
        return self.lines[line - 1] + col
    def handle_starttag(self, tag, attrs):
        start = self.source_offset()
        node = {'tag':tag, 'attrs':dict(attrs), 'start':start, 'open_end':start+len(self.get_starttag_text()), 'children':[], 'parent':self.stack[-1] if self.stack else None}
        node['style'] = dict(pair.strip().split(':',1) for pair in node['attrs'].get('style','').split(';') if ':' in pair)
        node['style'] = {k:v.strip() for k,v in node['style'].items()}
        node['name'] = node['attrs'].get('data-pencil-name','')
        if self.stack: self.stack[-1]['children'].append(node)
        self.nodes.append(node)
        if tag not in VOID: self.stack.append(node)
        else: node['close_start'] = node['end'] = node['open_end']
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID: self.handle_endtag(tag)
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1]['tag'] == tag:
            node = self.stack.pop()
            node['close_start'] = self.source_offset()
            node['end'] = self.html.find('>',self.source_offset())+1
    def named(self, name): return next(n for n in self.nodes if n['name']==name)
    def markup(self, node): return self.html[node['start']:node['end']]

def replace_ranges(html, edits):
    for start,end,value in sorted(edits,reverse=True): html=html[:start]+value+html[end:]
    return html
