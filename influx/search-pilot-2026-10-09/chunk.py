"""Pilot chunker for ref/canonical/KEY.md (search pilot, 2026-10-09).

Not the index's chunker: a sketch to learn what the real one (search/DESIGN.md §5)
has to handle. It parses a canonical text into blocks, carrying page, printed
label and heading path, elects a section kind, detects definitions, and packs
blocks into passages of about `target` characters of *indexed* text. Every
passage keeps [start, end) offsets into the canonical file, so displayed text
and anchors use the file's own characters.

    python3 chunk.py KEY [--target 1200] [--show]
"""
import bisect, json, os, re, sys
sys.dont_write_bytecode = True   # importing bin/corpus.py would otherwise write bin/__pycache__ into the repo

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, 'bin'))
import corpus  # noqa: E402

CANON = os.path.join(REPO, 'ref', 'canonical')

# ------------------------------------------------------------------ cleaning
IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]*\)')
# [text](target "tooltip") -- IASR's web edition carries a full reference in the tooltip
LINK_RE = re.compile(r'\[([^\]]*)\]\((?:<[^>]*>|[^\s)]+)(?:\s+"(?:[^"\\]|\\.)*")?\)')
TAG_RE = re.compile(r'</?(?:span|a|sup|sub|div|i|b|em|strong|u)\b[^>]*>', re.I)
SUP_NUM_RE = re.compile(r'<sup>\s*[\d,\s–-]+\s*</sup>', re.I)
BR_RE = re.compile(r'<br\s*/?>', re.I)

def clean(s, keep_emphasis=False):
    s = IMG_RE.sub(' ', s)
    s = LINK_RE.sub(lambda m: '' if re.fullmatch(r'[\d,\s–-]*', m.group(1)) else m.group(1), s)
    s = SUP_NUM_RE.sub(' ', s)
    s = BR_RE.sub(' ', s)
    s = TAG_RE.sub('', s)
    s = s.replace('\\$', '$').replace('\\_', '_').replace('\\*', '*')
    if not keep_emphasis:
        s = re.sub(r'\*\*|__', '', s)
        s = re.sub(r'(?<![\w*])\*(?=\S)([^*\n]+?)(?<=\S)\*(?![\w*])', r'\1', s)
    s = re.sub(r'^\|?[\s|:-]{3,}\|?$', '', s, flags=re.M)          # table rule rows
    s = re.sub(r'[ \t]+', ' ', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()

def clean_heading(h):
    h = clean(h)
    return re.sub(r'\s+', ' ', h).strip(' :')

# ------------------------------------------------------------ section kinds
SECTION_PATTERNS = [
    ('glossary', re.compile(r'^(glossary( of terms)?|definitions?|terminology|key terms|key definitions|definitions and abbreviations|glossary and abbreviations)$', re.I)),
    ('toc', re.compile(r'^(table of )?contents$', re.I)),
    ('references', re.compile(r'^(references|bibliography|notes|endnotes|works cited|citations)$', re.I)),
    ('abbreviations', re.compile(r'\b(abbreviations|acronyms)\b', re.I)),
    ('annex', re.compile(r'^(annex|appendix)\b', re.I)),
]

def heading_kind(h):
    core = re.sub(r'^[\dA-Z]{0,3}(\.\d+)*\.?\s+', '', h).strip()
    for kind, pat in SECTION_PATTERNS:
        if pat.search(core if kind != 'annex' else h):
            return kind
    return None

# -------------------------------------------------------------- definitions
Q_OPEN, Q_CLOSE = '"“‘\'', '"”’\''
QT = r'["“‘\']([^"”’\'\n]{2,70}?)["”’\']'
# the optional ", for the purpose of …," catches AI Act Art. 3(58) ('subject', for the purpose of
# real-world testing, means …), the one of 68 the pilot's runs missed; fixed after those runs
STAT_RE = re.compile(r'^\s*(?:-\s*)?(?:\(\w{1,4}\)\s*)+' + QT + r'(?:,[^,\n]{1,80},)?\s+(?:means|shall mean|has the meaning)\b')
GLOSS_BOLD_RE = re.compile(r'^\s*(?:-\s*(?:\(\w{1,4}\)\s*)?)?\*\*([^*\n]{2,90}?):\*\*\s*\S')
GLOSS_BOLD2_RE = re.compile(r'^\s*(?:-\s*(?:\(\w{1,4}\)\s*)?)?\*\*([^*\n]{2,90}?)\*\*:\s*\S')
INLINE_RES = [
    ('inline-we-mean', 0.9, re.compile(r'\bby\s+' + QT + r',?\s+(?:in this [a-z]+,?\s+)?we mean\b', re.I)),
    ('inline-quoted', 0.8, re.compile(QT + r',?\s+(?:means|shall mean|refers to|is defined as|denotes|is used to mean)\b', re.I)),
    ('inline-we-define', 0.8, re.compile(r'\bwe (?:define|use(?: the term)?)\s+\*?["“‘\']?([A-Za-z][\w\s-]{1,50}?)["”’\']?\*?\s+(?:as|to mean)\b', re.I)),
    ('inline-which-we-define', 0.8, re.compile(r'\*([A-Za-z][^*\n]{1,50})\*,?\s+which we define as', re.I)),
    ('inline-emph-refers', 0.7, re.compile(r'\*([A-Za-z][^*\n]{1,50})\*\s+(?:refers to|means|is defined as)\b', re.I)),
    ('inline-defined-as', 0.5, re.compile(r'\b(?:we )?defined?\s+([a-z][a-z -]{1,40}?)\s+as\s+(?:the|a|an)\b', re.I)),
]

def norm_term(t):
    t = clean(t).lower()
    t = re.sub(r'[\'"“”‘’*_]', '', t)
    t = re.sub(r'\([^)]*\)', ' ', t)          # "Floating point operations (FLOP)"
    t = re.sub(r'[^\w\s-]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    words = t.split()
    if words:
        w = words[-1]
        if len(w) > 3 and w.endswith('s') and not w.endswith(('ss', 'us', 'is')):
            words[-1] = w[:-1]
    return ' '.join(words)

# ------------------------------------------------------------------ parsing
HEAD_RE = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')
STAT_SEC_RE = re.compile(r'^-?\s*\*\*(?:SEC(?:TION)?\.\s*)?(\d[\d.]*\d?)\.\*\*')  # - **22757.12.** (a) …

def parse(key):
    path = os.path.join(CANON, key + '.md')
    raw = open(path, encoding='utf-8').read()
    # page markers: (offset, page, printed, not_in_pdf)
    marks = []
    for m in re.finditer(r'^.*$', raw, re.M):
        mm = corpus.MARK_RE.match(m.group(0))
        if mm:
            marks.append((m.start(), int(mm.group(1)) if mm.group(1) else None, mm.group(2), mm.group(1) is None))
    blocks, heads = [], []          # heads: [(level, text)]
    lines = [(m.start(), m.group(0)) for m in re.finditer(r'^.*$', raw, re.M)]
    i, n = 0, len(lines)
    in_comment = False
    stat_sec = None
    def hpath():
        p = [h for _, h in heads]
        if stat_sec:
            p = p + [stat_sec]
        return p
    while i < n:
        off, line = lines[i]
        if in_comment or line.startswith('<!--'):
            in_comment = '-->' not in line
            i += 1
            continue
        if not line.strip() or corpus.MARK_RE.match(line):
            i += 1
            continue
        hm = HEAD_RE.match(line)
        if hm:
            lvl, text = len(hm.group(1)), clean_heading(hm.group(2))
            while heads and heads[-1][0] >= lvl:
                heads.pop()
            heads.append((lvl, text))
            stat_sec = None
            blocks.append(dict(start=off, end=off + len(line), kind='heading', path=hpath(), raw=line))
            i += 1
            continue
        if line.startswith(corpus.SUPP_OPEN):
            j = i + 1
            while j < n and lines[j][1] != corpus.SUPP_CLOSE:
                j += 1
            end = lines[min(j, n - 1)][0] + len(lines[min(j, n - 1)][1])
            body = raw[lines[i][0] + len(line) + 1: lines[min(j, n - 1)][0]]
            blocks.append(dict(start=off, end=end, kind='pdftext', path=hpath(), raw=body,
                               body_start=lines[i][0] + len(line) + 1))
            i = j + 1
            continue
        if line.lstrip().startswith('|'):
            j = i
            rows = []
            while j < n and (lines[j][1].lstrip().startswith('|') or corpus.MARK_RE.match(lines[j][1])
                             or (not lines[j][1].strip() and j + 1 < n and
                                 (lines[j + 1][1].lstrip().startswith('|') or corpus.MARK_RE.match(lines[j + 1][1])))):
                if lines[j][1].lstrip().startswith('|'):
                    rows.append(lines[j])
                j += 1
            blocks.append(dict(start=off, end=rows[-1][0] + len(rows[-1][1]), kind='table', path=hpath(), rows=rows))
            i = j
            continue
        if re.match(r'^\s*-\s', line) and not line.startswith(' '):
            sm = STAT_SEC_RE.match(line)
            if sm:
                stat_sec = '§' + sm.group(1)
            j = i + 1
            while j < n and lines[j][1].startswith((' ', '\t')) and lines[j][1].strip():
                j += 1
            end = lines[j - 1][0] + len(lines[j - 1][1])
            blocks.append(dict(start=off, end=end, kind='item', path=hpath(), raw=raw[off:end]))
            i = j
            continue
        # paragraph: until blank line
        j = i + 1
        while j < n and lines[j][1].strip() and not corpus.MARK_RE.match(lines[j][1]) \
                and not HEAD_RE.match(lines[j][1]) and not lines[j][1].lstrip().startswith(('|', '- ')):
            j += 1
        end = lines[j - 1][0] + len(lines[j - 1][1])
        txt = raw[off:end]
        if IMG_RE.fullmatch(txt.strip()):
            i = j
            continue
        sm = STAT_SEC_RE.match(line)
        if sm:
            stat_sec = '§' + sm.group(1)
            for b in blocks[-1:]:
                pass
        blocks.append(dict(start=off, end=end, kind='para', path=hpath(), raw=txt))
        i = j
    return raw, marks, blocks

# ------------------------------------------------------------ page lookup
class Pages:
    def __init__(self, marks):
        self.offs = [m[0] for m in marks]
        self.marks = marks
    def at(self, off):
        k = bisect.bisect_right(self.offs, off) - 1
        if k < 0:
            return (None, None, False)
        _, p, pr, nip = self.marks[k]
        return (p, pr, nip)
    def span(self, a, b):
        """distinct physical pages touched by [a, b)"""
        k0 = max(0, bisect.bisect_right(self.offs, a) - 1)
        k1 = bisect.bisect_left(self.offs, b)
        out = []
        for k in range(k0, max(k0 + 1, k1)):
            if k < len(self.marks):
                p = self.marks[k][1]
                if p not in out:
                    out.append(p)
        return out

# ------------------------------------------------------- definitions detect
def detect_block_defs(b, section_kind):
    """Structural and wording evidence that a block defines a term."""
    defs = []
    first = b.get('raw', '').split('\n', 1)[0] if b['kind'] in ('item', 'para') else ''
    m = STAT_RE.match(first)
    if m:
        defs.append(dict(term=m.group(1), kind='statutory-means', conf=0.95, evidence='"X" means'))
    m = GLOSS_BOLD_RE.match(first) or GLOSS_BOLD2_RE.match(first)
    if m and re.match(r'(figure|table|box|note|claim)\b', m.group(1).strip(), re.I):
        m = None
    if m and not defs:
        b['numbered'] = bool(re.match(r'^\s*-\s*\(\w{1,4}\)', first))
        b['bold_lead'] = m.group(1)
        if section_kind == 'glossary':
            defs.append(dict(term=m.group(1), kind='glossary-entry', conf=0.9, evidence='**Term:** in glossary section'))
    if b['kind'] in ('item', 'para'):
        body = clean(b['raw'], keep_emphasis=True)
        for kind, conf, rx in INLINE_RES:
            for mm in rx.finditer(body):
                t = mm.group(1).strip().strip('*').strip()
                if len(t.split()) > 7 or re.match(r'(by|in|a|an|the|these|this|that|its|their|our)\b', t, re.I) \
                        or t.endswith(','):
                    continue
                kk = 'footnote-' + kind if b['raw'].lstrip().startswith('<sup>') or b['raw'].lstrip().startswith('<span') and '<sup>' in b['raw'][:60] else kind
                if not any(norm_term(d['term']) == norm_term(t) for d in defs):
                    defs.append(dict(term=t, kind=kk, conf=conf, evidence=mm.group(0)[:80]))
    return defs

def elect_bold_runs(blocks):
    """A heading-less glossary: a run of >=5 '**Term:** text' paragraphs whose
    terms are in alphabetical order. A non-alphabetical run is a key-points box:
    its leads are recorded as weak definitions."""
    i = 0
    while i < len(blocks):
        if blocks[i].get('bold_lead') is None:
            i += 1
            continue
        j = i
        while j < len(blocks) and (blocks[j].get('bold_lead') is not None or blocks[j]['kind'] == 'heading' and False):
            j += 1
        run = blocks[i:j]
        terms = [norm_term(b['bold_lead']) for b in run]
        asc = sum(1 for a, c in zip(terms, terms[1:]) if a <= c) / max(1, len(terms) - 1)
        if len(run) >= 5 and asc >= 0.85:
            for b in run:
                if b['section'] in ('body', 'annex'):
                    b['section'] = 'glossary'
                    # the run has no heading of its own; the inherited path is wrong
                    b['path'] = b['path'][:1] + ['Glossary (no heading in source)']
                if not any(d['kind'] == 'glossary-entry' for d in b['defs']):
                    b['defs'].insert(0, dict(term=b['bold_lead'], kind='glossary-entry', conf=0.85,
                                             evidence=f'alphabetical run of {len(run)} **Term:** paragraphs'))
                b['standalone'] = True
        elif len(run) >= 2:
            for b in run:
                if not b['defs']:
                    b['defs'].append(dict(term=b['bold_lead'], kind='bold-lead', conf=0.5 if b.get('numbered') else 0.35,
                                          evidence=f'non-alphabetical run of {len(run)} **Label:** paragraphs'))
        i = j

def table_rows(b):
    """Group table rows into (header, [row groups]); a row whose first cell is
    empty continues the row above (the EU Code's glossary wraps that way)."""
    rows = b['rows']
    header = None
    groups = []
    for k, (off, line) in enumerate(rows):
        if re.fullmatch(r'\s*\|?[\s|:-]+\|?\s*', line):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        nxt_rule = k + 1 < len(rows) and re.fullmatch(r'\s*\|?[\s|:-]+\|?\s*', rows[k + 1][1])
        if header is None and nxt_rule and k == 0:
            header = (off, line, cells)
            continue
        if groups and (not cells[0]):
            groups[-1].append((off, line, cells))
        else:
            groups.append([(off, line, cells)])
    return header, groups

# ------------------------------------------------------------------ passages
def passages(key, target=1200, maxlen=None, min_standalone=True):
    raw, marks, blocks = parse(key)
    pages = Pages(marks)
    maxlen = maxlen or int(target * 1.4)
    # section kinds by heading path
    for b in blocks:
        sk = 'body'
        for depth, h in enumerate(b['path']):
            k = heading_kind(h)
            # a table of contents covers only its own heading's blocks: IASR nests
            # front matter (Secretariat, Scope…) under "Table of contents"
            if k and (k != 'toc' or depth == len(b['path']) - 1):
                sk = k
        b['section'] = sk
    # tables become row-group pseudo-blocks
    out_blocks = []
    for b in blocks:
        if b['kind'] != 'table':
            b['defs'] = detect_block_defs(b, b['section'])
            out_blocks.append(b)
            continue
        header, groups = table_rows(b)
        for g in groups:
            first_cell = g[0][2][0] if g[0][2] else ''
            sub = dict(start=g[0][0], end=g[-1][0] + len(g[-1][1]), kind='tablerow', path=b['path'],
                       section=b['section'], header=header, raw='\n'.join(x[1] for x in g), defs=[])
            if b['section'] == 'glossary' and re.match(r'^\s*(\*\*)?["“‘\']', first_cell):
                sub['defs'].append(dict(term=clean(first_cell), kind='glossary-table-row', conf=0.9,
                                        evidence='quoted term in first cell, glossary section'))
                sub['standalone'] = True
            out_blocks.append(sub)
    blocks = out_blocks
    elect_bold_runs(blocks)
    for b in blocks:
        if any(d['conf'] >= 0.8 and d['kind'] in ('statutory-means', 'glossary-entry', 'glossary-table-row')
               for d in b['defs']):
            b['standalone'] = True
        # a '**Label:** text' paragraph or item is a self-contained unit (the EU Code's
        # "(2) Loss of control: Risks from …", IASR's key-information boxes). Packed with
        # its siblings, its embedding is the average of four risks (pilot, v1 → v2).
        if b.get('bold_lead') and len(clean(b.get('raw', ''))) >= 80:
            b['standalone'] = True

    def text_of(b):
        if b['kind'] == 'heading':
            return ''
        if b['kind'] == 'tablerow':
            rows = [b['raw']]
            if b.get('header'):
                rows.insert(0, b['header'][1])
            return clean('\n'.join(rows))
        return clean(b.get('raw', ''))

    out = []
    cur = []

    def flush():
        if not cur:
            return
        bs = [b for b in cur if b['kind'] != 'heading']
        if not bs:
            cur.clear()
            return
        start, end = bs[0]['start'], bs[-1]['end']
        txt = '\n\n'.join(t for t in (text_of(b) for b in bs) if t)
        if not txt.strip():
            cur.clear()
            return
        p0, pr0, nip = pages.at(start)
        defs = [d for b in bs for d in b['defs']]
        for d in defs:
            d['norm'] = norm_term(d['term'])
        out.append(dict(key=key, start=start, end=end, page=p0, printed=pr0,
                        pages=pages.span(start, end), not_in_pdf=any(pages.at(b['start'])[2] for b in bs),
                        path=bs[0]['path'], section=bs[0]['section'],
                        kinds=sorted({b['kind'] for b in bs}), text=txt, defs=defs))
        cur.clear()

    def size(bs):
        return sum(len(text_of(b)) for b in bs)

    for b in blocks:
        if b['kind'] == 'heading':
            flush()
            continue
        if cur and cur[-1]['path'] != b['path']:
            flush()
        if b.get('standalone') and min_standalone:
            flush()
            cur.append(b)
            flush()
            continue
        t = text_of(b)
        if len(t) > maxlen:
            flush()
            # split a long block at sentence boundaries, keeping offsets approximate (block-level)
            sents = re.split(r'(?<=[.;:])\s+(?=[A-Z(“"‘\'-])', t)
            acc = ''
            for s in sents:
                if acc and len(acc) + len(s) > target:
                    out.append(_split_piece(key, b, acc, pages, raw))
                    acc = s
                else:
                    acc = (acc + ' ' + s).strip()
            if acc:
                out.append(_split_piece(key, b, acc, pages, raw))
            continue
        if cur and size(cur) + len(t) > target:
            flush()
        cur.append(b)
    flush()
    for k, p in enumerate(out):
        p['id'] = f'{key}#{k}'
    return out, raw

def _split_piece(key, b, txt, pages, raw):
    """A piece of a long block. Locate it in the raw block by its first words."""
    probe = re.escape(' '.join(txt.split()[:6]))
    probe = probe.replace(r'\ ', r'[\s\S]{1,40}?')
    seg = raw[b['start']:b['end']]
    m = re.search(probe, seg)
    start = b['start'] + (m.start() if m else 0)
    p0, pr0, nip = pages.at(start)
    defs = [dict(d, norm=norm_term(d['term'])) for d in b['defs'] if norm_term(d['term']).split()[0] in txt.lower()] if b['defs'] else []
    return dict(key=key, start=start, end=min(b['end'], start + int(len(txt) * 1.6)), page=p0, printed=pr0,
                pages=pages.span(start, start + len(txt)), not_in_pdf=nip, path=b['path'], section=b['section'],
                kinds=[b['kind'] + '-split'], text=txt, defs=defs)

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('key')
    ap.add_argument('--target', type=int, default=1200)
    ap.add_argument('--show', action='store_true')
    ap.add_argument('--defs', action='store_true')
    a = ap.parse_args()
    ps, raw = passages(a.key, a.target)
    lens = sorted(len(p['text']) for p in ps)
    print(f'{a.key}: {len(ps)} passages; chars median {lens[len(lens)//2]}, p90 {lens[int(len(lens)*.9)]}, max {lens[-1]}; '
          f'{sum(1 for p in ps if p["defs"])} with definitions; sections ' +
          json.dumps({s: sum(1 for p in ps if p['section'] == s) for s in sorted({p['section'] for p in ps})}))
    for p in ps:
        if a.defs and p['defs']:
            for d in p['defs']:
                print(f"  p{p['page']:>4} {d['kind']:<22} {d['conf']:.2f} {d['term'][:50]!r:<52} {' › '.join(p['path'])[-60:]}")
        if a.show:
            print('-' * 80)
            print(p['id'], p['page'], p['pages'], p['section'], p['kinds'], ' › '.join(p['path']))
            print(p['text'][:600])
