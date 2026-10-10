"""Render CAML bill XML (California Legislative Counsel) to text.
Tracks Legislative Counsel's own amendment marks:
  <?xm-insertion_mark_start?> ... <?xm-insertion_mark_end?>  = text added in this version
  <?xm-deletion_mark data="..."?>                            = text struck in this version (escaped markup)
Modes: clean (as amended), pre (insertions dropped, deletions kept), marked (wdiff-style {+ +} [- -]).
"""
import re, sys, html
TOK = re.compile(r'(<\?.*?\?>|<!--.*?-->|<[^>]+>)', re.S)
BLOCK = {'p','Num','ActionLine','LawHeadingText','Preamble','Title',
         'Subject','AuthorText','BillSection','LawSection','LawHeading',
         'DigestText','Content','Fragment','LawSectionVersion'}
SKIP = {'History','Authors','LegislativeInfo','DigestKey','MeasureIndicators',
        'Id','VersionNum','RelatingClause','ChapterYear','ChapterType',
        'ChapterSessionNum','ChapterNum'}
def local(name):
    # element name without namespace prefix (works for caml:, xhtml:, html:, ns0: ...)
    n = name.split()[0].strip('/')
    return n.split(':')[-1]
def events(s, state='n', out=None, skip=None):
    """yield (kind, value, state) ; kind in text|brk|open"""
    if out is None: out=[]
    if skip is None: skip=[0]
    ins = [state]
    for t in TOK.split(s):
        if not t: continue
        if t.startswith('<?'):
            if t.startswith('<?xm-insertion_mark_start'): ins.append('i')
            elif t.startswith('<?xm-insertion_mark_end'): ins.pop() if len(ins)>1 else None
            elif t.startswith('<?xm-deletion_mark'):
                m = re.match(r'<\?xm-deletion_mark data="(.*)"\?>$', t, re.S)
                data = html.unescape(m.group(1)) if m else ''
                events(data, 'd', out, skip)
            continue
        if t.startswith('<!--'): continue
        if t.startswith('<'):
            closing = t.startswith('</'); selfc = t.endswith('/>')
            name = local(t[2:-1] if closing else t[1:-1])
            if name in SKIP:
                if not selfc: skip[0] += -1 if closing else 1
                continue
            if skip[0]: continue
            if name == 'span' and 'EnSpace' in t: out.append(('text',' ',ins[-1])); continue
            if name == 'LawHeading' and not closing:
                m = re.search(r'type="([A-Z]+)"', t); out.append(('brk','',ins[-1]))
                out.append(('text',(m.group(1).title() if m else '')+' ',ins[-1])); continue
            if name == 'DigestText' and not closing:
                out.append(('brk','',ins[-1])); out.append(('text',"LEGISLATIVE COUNSEL'S DIGEST",ins[-1])); out.append(('brk','',ins[-1])); continue
            if name == 'Bill' and not closing:
                out.append(('brk','',ins[-1])); out.append(('text','BILL TEXT',ins[-1])); out.append(('brk','',ins[-1])); continue
            if name in BLOCK: out.append(('brk','',ins[-1]))
            continue
        if skip[0]: continue
        txt = html.unescape(t)
        txt = re.sub(r'\s+', ' ', txt)
        out.append(('text', txt, ins[-1]))
    return out
def render(s, mode):
    ev = events(s)
    paras=[]; cur=[]
    def flush():
        line=''.join(cur); line=re.sub(r' {2,}',' ',line).strip()
        # tidy marker spacing
        if line and line not in ('{++}','[--]'): paras.append(line)
        cur.clear()
    st='n'
    def setstate(new):
        nonlocal st
        if mode!='marked' or new==st: st=new; return
        if st=='i': cur.append('+}')
        if st=='d': cur.append('-]')
        if new=='i': cur.append('{+')
        if new=='d': cur.append('[-')
        st=new
    for kind,val,state in ev:
        if kind=='brk':
            setstate('n'); flush(); continue
        if mode=='clean' and state=='d': continue
        if mode=='pre' and state=='i': continue
        if mode in('clean','pre'): cur.append(val); continue
        setstate(state); cur.append(val)
    setstate('n'); flush()
    # remove empty marker pairs
    out=[]
    for p in paras:
        p=re.sub(r'\{\+\s*\+\}','',p); p=re.sub(r'\[-\s*-\]','',p); p=re.sub(r' {2,}',' ',p).strip()
        if p: out.append(p)
    return out
if __name__=='__main__':
    src, mode = sys.argv[1], sys.argv[2]
    print('\n\n'.join(render(open(src,encoding='utf-8').read(), mode)))
