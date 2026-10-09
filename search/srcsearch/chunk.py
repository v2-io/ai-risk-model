"""A canonical text cut into blocks, then into passages (DESIGN §5).

Blocks are the canonical markdown's own units: headings, paragraphs, list items,
tables, and ```pdf-text blocks (text restored from the PDF's text layer). Each
carries its page, from the `[pdf-page N, printed "X"]` markers, its heading path,
and its section kind.

Passages are what the index stores and ranks. The rules, and the pilot findings
behind them (influx/search-pilot-2026-10-09/REPORT.md §5):
- about 1,200 characters of indexed text, never across a heading;
- one entry, one passage: a statutory definition, a glossary entry or row, and a
  `**Label:** text` item stand alone. Packed with its three sibling risks, the
  EU Code's "(2) Loss of control: …" ranked 381st semantically for "loss of
  control"; standalone, in the top 3;
- a block holding a definition runs long rather than being cut (up to
  DEF_MAXLEN), because the pilot found definitions split mid-sentence;
- a longer block is cut at sentence boundaries, with one sentence of overlap,
  at offsets exact to the character (text.Mapped);
- a statute's section numbers inside list items (`- **22757.12.** (a) …`) act as
  headings;
- a table of contents covers only its own heading's blocks: IASR nests its front
  matter under "Table of contents";
- restored ```pdf-text blocks sit at the end of their page's section in the
  canonical text, not where they stood on the page, so they carry no heading
  path and have their own section kind (the NRR's carry its risk-matrix legend,
  "140 Catastrophic 5 Significant 4 …", which otherwise matches "catastrophic").
"""
import bisect, hashlib, re

from . import defs as D
from .text import Mapped, clean, clean_heading, norm_passage, norm_term, sentences
import corpus

TARGET = 1200            # characters of indexed text
MAXLEN = 1700            # a single block longer than this is cut
DEF_MAXLEN = 4000        # ... unless it holds a definition, which runs long up to this

HEAD_RE = re.compile(r'^(#{1,6})\s+(.*\S)\s*$')
ITEM_RE = re.compile(r'^(?:[-*+•]|\d{1,3}[.)])\s')
TABLE_RE = re.compile(r'^\s*\|')
# A statute's section number at the start of a list item or paragraph acts as a heading:
# `- **22757.12.** (a) …` (a code section) and `- **SEC. 3.** Section 11546.8 is added …` (a bill section).
STAT_SEC_RE = re.compile(r'^(?:[-*+]\s*)?\*\*((?:SEC(?:TION)?\.?\s*)?)(\d+(?:\.\d+)*[A-Z]?)\.?\*\*')
SEC_HEAD_RE = re.compile(r'^(?:SEC(?:TION)?\.?)\s*\d+[A-Z]?\.?(?:\s|$)')            # SECTION 1. The Legislature …
CODE_HEAD_RE = re.compile(r'^§?\s*\d{3,}(?:\.\d+)*\.?(?:\s|$)')                     # 22757.11. For purposes …


# A heading that is only a structural label: "Article 3", "ANNEX I", "CHAPTER III", "SECTION 2".
# Conversions give these arbitrary markdown levels (the AI Act's "# *Article 4*" is level 1
# and its title "### **…**" level 3), so they nest by kind, and the title heading that
# follows directly becomes part of the label: "Article 3 — Definitions".
LABEL_RE = re.compile(r'^(part|title|chapter|section|article|annex|appendix|schedule)\s+([0-9]+[A-Z]?|[IVXLC]+)\.?$', re.I)
LABEL_RANK = dict(part=1, title=2, chapter=3, annex=3, appendix=3, schedule=3, section=4, article=5)


def sec_class(text):
    return 'sec' if SEC_HEAD_RE.match(text) else 'code' if CODE_HEAD_RE.match(text) else None


IMG_ONLY_RE = re.compile(r'^\s*(?:!\[[^\]\n]*\]\([^)\n]*\)\s*)+$')

SECTION_PATTERNS = [
    ('glossary', re.compile(r'^(?:glossary(?: of terms)?|definitions?|terminology|key terms|key definitions|'
                            r'definitions and abbreviations|glossary and abbreviations|terms and definitions)$', re.I)),
    ('toc', re.compile(r'^(?:table of )?contents$', re.I)),
    ('references', re.compile(r'^(?:references|bibliography|notes|endnotes|works cited|citations|sources)$', re.I)),
    ('abbreviations', re.compile(r'\b(?:abbreviations|acronyms)\b', re.I)),
    ('index', re.compile(r'^index$', re.I)),
    ('annex', re.compile(r'^(?:annex|appendix|appendices)\b', re.I)),
]


def heading_kind(h):
    if ' — ' in h and LABEL_RE.match(h.split(' — ')[0]) and not h.lower().startswith(('annex', 'appendix')):
        h = h.split(' — ', 1)[1]                  # "Article 3 — Definitions": the title says what it holds
    core = re.sub(r'^(?:[\dA-Z]{1,3}(?:\.\d+)*\.?|[IVX]+\.)\s+', '', h).strip()
    for kind, pat in SECTION_PATTERNS:
        if pat.search(core if kind != 'annex' else h):
            return kind
    return None


class Pages:
    """Physical page and printed label at an offset, from the marker lines."""

    def __init__(self, raw):
        self.marks = []                          # (offset, page or None, printed or None, not_in_pdf)
        for m in re.finditer(r'^----------\[[^\n]*$', raw, re.M):
            mm = corpus.MARK_RE.match(m.group(0))
            if mm:
                self.marks.append((m.start(), int(mm.group(1)) if mm.group(1) else None,
                                   mm.group(2), mm.group(1) is None))
        self.offs = [m[0] for m in self.marks]

    def at(self, off):
        k = bisect.bisect_right(self.offs, off) - 1
        return (None, None, False) if k < 0 else self.marks[k][1:]

    def span(self, a, b):
        """Physical pages touched by [a, b), in text order (they can run backwards)."""
        k0 = max(0, bisect.bisect_right(self.offs, a) - 1)
        k1 = bisect.bisect_left(self.offs, b)
        out = []
        for k in range(k0, max(k0 + 1, k1)):
            if k < len(self.marks) and self.marks[k][1] not in out:
                out.append(self.marks[k][1])
        return [p for p in out if p is not None] or [None]

    def not_in_pdf(self, a, b):
        k0 = max(0, bisect.bisect_right(self.offs, a) - 1)
        k1 = bisect.bisect_left(self.offs, b)
        return any(self.marks[k][3] for k in range(k0, max(k0 + 1, k1)) if k < len(self.marks))


# ---------------------------------------------------------------------- blocks
def parse(raw):
    """(blocks, headings). A block: start, end (offsets into raw), kind, path."""
    lines = [(m.start(), m.group(0)) for m in re.finditer(r'^.*$', raw, re.M)]
    n = len(lines)
    blocks, headings = [], []
    heads = []                    # [[markdown level, text, statute class, label rank or None]]
    label_open = [False]          # a label heading was just read, with nothing after it yet
    in_comment = False

    def path():
        return [h[1] for h in heads]

    def add_block(b):
        blocks.append(b)
        label_open[0] = False

    def heading(lvl, text):
        lm = LABEL_RE.match(text)
        if lm:
            rank = LABEL_RANK[lm.group(1).lower()]
            while heads and not (heads[-1][3] is not None and heads[-1][3] < rank):
                heads.pop()                              # (a contents heading included)
            heads.append([lvl, text, None, rank])
            label_open[0] = True
            return True
        if label_open[0] and heads and heads[-1][3] is not None:
            heads[-1][1] += ' — ' + text                # the label's title
            label_open[0] = False
            return False
        while heads and heads[-1][3] is None and heads[-1][0] >= lvl:
            heads.pop()
        # a table of contents holds only itself: IASR and AISI put their whole front
        # matter in headings below "Table of contents"
        while heads and heading_kind(heads[-1][1]) == 'toc':
            heads.pop()
        heads.append([lvl, text, sec_class(text), None])
        return True

    def statute_section(line):
        """A section number opening an item or paragraph replaces the heading of the
        previous section of its own class, at that heading's level: SEC. 3 replaces
        SEC. 2 (or the SECTION 1 heading), §22757.13 replaces §22757.12. A code section
        sits inside the bill section that adds it, so it never replaces one."""
        m = STAT_SEC_RE.match(line)
        if not m:
            return
        cls = 'sec' if m.group(1) else 'code'
        label = ('SEC. ' if cls == 'sec' else '§') + m.group(2)
        k = len(heads) - 1
        while k >= 0 and heads[k][2] != cls and heads[k][3] is None and not (cls == 'code' and heads[k][2] == 'sec'):
            k -= 1
        if k >= 0 and heads[k][2] == cls:
            lvl = heads[k][0]
            del heads[k:]
        else:
            lvl = heads[-1][0] + 1 if heads else 1
        heads.append([lvl, label, cls, None])

    def starts_block(line):
        return (not line.strip() or corpus.MARK_RE.match(line) or HEAD_RE.match(line) or TABLE_RE.match(line)
                or ITEM_RE.match(line) or line.startswith(corpus.SUPP_OPEN) or line.startswith('<!--'))

    i = 0
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
            if text:
                if heading(lvl, text):
                    headings.append(dict(start=off, end=off + len(line), level=lvl, text=text, path=path()))
                else:                                   # merged into the label before it
                    headings[-1]['title'] = text
                    headings[-1]['path'] = path()
            i += 1
            continue
        if line.startswith(corpus.SUPP_OPEN):
            j = i + 1
            while j < n and lines[j][1] != corpus.SUPP_CLOSE:
                j += 1
            j = min(j, n - 1)
            body_start = off + len(line) + 1
            if lines[j][0] > body_start:
                add_block(dict(start=body_start, end=lines[j][0] - 1, kind='restored', path=[]))
            i = j + 1
            continue
        if TABLE_RE.match(line):
            j, rows = i, []
            while j < n:
                l = lines[j][1]
                if TABLE_RE.match(l):
                    rows.append(lines[j])
                elif corpus.MARK_RE.match(l) or (not l.strip() and j + 1 < n and
                                                 (TABLE_RE.match(lines[j + 1][1]) or corpus.MARK_RE.match(lines[j + 1][1]))):
                    pass                          # a table runs on across a page marker
                else:
                    break
                j += 1
            add_block(dict(start=off, end=rows[-1][0] + len(rows[-1][1]), kind='table', path=path(), rows=rows))
            i = j
            continue
        if ITEM_RE.match(line):
            statute_section(line)
            j = i + 1
            while j < n and lines[j][1][:1] in (' ', '\t') and lines[j][1].strip():
                j += 1
            end = lines[j - 1][0] + len(lines[j - 1][1])
            add_block(dict(start=off, end=end, kind='item', path=path()))
            i = j
            continue
        j = i + 1
        while j < n and not starts_block(lines[j][1]):
            j += 1
        end = lines[j - 1][0] + len(lines[j - 1][1])
        # a paragraph cut by a page break: it starts in lower case, and only the
        # page marker stands between it and the block it continues
        # (and the block before doesn't end a sentence: footnotes often stand between the two)
        if (blocks and blocks[-1]['kind'] in ('para', 'item') and line[:1].islower()
                and not re.search(r'[.!?:;]["”’)]*\s*$', raw[blocks[-1]['start']:blocks[-1]['end']])
                and all(not l.strip() or corpus.MARK_RE.match(l) for l in raw[blocks[-1]['end']:off].split('\n'))
                and blocks[-1]['path'] == path()):
            blocks[-1]['end'] = end
            blocks[-1]['joined_page_break'] = True
            i = j
            continue
        if not IMG_ONLY_RE.match(raw[off:end]):
            statute_section(line)
            add_block(dict(start=off, end=end, kind='para', path=path()))
        i = j
    return blocks, headings


def _sections(blocks):
    for b in blocks:
        sk = 'restored' if b['kind'] == 'restored' else 'body'
        if b['kind'] != 'restored':
            for depth, h in enumerate(b['path']):
                k = heading_kind(h)
                if k and (k != 'toc' or depth == len(b['path']) - 1):
                    sk = k
        b['section'] = sk


def _table_groups(raw, b):
    """(header line or None, [[(offset, line, cells)], …]): rows grouped, a row
    whose first cell is empty continuing the one above (the EU Code's glossary
    wraps that way, across rows and pages)."""
    rule = re.compile(r'\s*\|?[\s|:-]+\|?\s*$')
    header, groups = None, []
    rows = b['rows']
    for k, (off, line) in enumerate(rows):
        if rule.fullmatch(line):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if k == 0 and k + 1 < len(rows) and rule.fullmatch(rows[k + 1][1]):
            # repeated with each group of rows, but only if it reads as a header: a
            # conversion can promote a first data row ("| 1 | AISI Research Agenda … |")
            if all(len(c) <= 60 for c in cells) and not re.fullmatch(r'[\d.()\[\]]+', cells[0] or 'x'):
                header = line
                continue
        if groups and not cells[0]:
            groups[-1].append((off, line, cells))
        else:
            groups.append([(off, line, cells)])
    return header, groups


# -------------------------------------------------------------------- passages
def passages(raw):
    """(passages, headings) for a canonical text. A passage: start, end (offsets
    into raw), text (indexed), pages, path, section, kinds, defs, norm_sha."""
    pages = Pages(raw)
    blocks, headings = parse(raw)
    _sections(blocks)
    for h in headings:
        p, pr, nip = pages.at(h['start'])
        h.update(page=p, printed=pr)

    units = []                                   # blocks, with tables turned into row groups
    for b in blocks:
        if b['kind'] != 'table':
            b['defs'] = D.detect(raw, b, b['section'])
            units.append(b)
            continue
        header, groups = _table_groups(raw, b)
        for g in groups:
            u = dict(start=g[0][0], end=g[-1][0] + len(g[-1][1]), kind='table', path=b['path'],
                     section=b['section'], header=header, defs=[])
            u['defs'] = D.table_row(raw, g[0][2][0] if g[0][2] else '', g[0][0], b['section'])
            if u['defs']:
                u['standalone'] = True
            units.append(u)
    D.elect_bold_runs(units)

    for u in units:
        u['text'] = _text(raw, u)
        if any(d['conf'] >= 0.8 for d in u['defs']):
            u['standalone'] = True
        if u.get('bold_lead') and len(u['text'].s) >= 80:
            u['standalone'] = True

    out, cur = [], []

    def emit(start, end, text, us, kinds=None):
        if not text.strip():
            return
        p0, pr0, nip0 = pages.at(start)
        p1, pr1, _ = pages.at(max(start, end - 1))
        ds = [dict(d, norm=norm_term(d['term'])) for u in us for d in u['defs'] if start <= d['at'] < end]
        out.append(dict(start=start, end=end, text=text, page=p0, printed=pr0, page_last=p1, printed_last=pr1,
                        pages=pages.span(start, end), not_in_pdf=pages.not_in_pdf(start, end),
                        path=us[0]['path'], section=us[0]['section'],
                        kinds=kinds or sorted({u['kind'] for u in us}), defs=ds,
                        norm_sha=hashlib.sha256(norm_passage(text).encode()).hexdigest()))

    def flush():
        if cur:
            emit(cur[0]['start'], cur[-1]['end'], '\n\n'.join(u['text'].s for u in cur if u['text'].s), list(cur))
            cur.clear()

    for u in units:
        if cur and (cur[-1]['path'] != u['path'] or cur[-1]['section'] != u['section']):
            flush()
        n = len(u['text'].s)
        limit = DEF_MAXLEN if u['defs'] else MAXLEN
        if n > limit:
            flush()
            for a, b in _cut(u['text']):
                s, e = u['text'].span(a, b)
                emit(s, e, u['text'].s[a:b], [u], kinds=[u['kind'], 'cut'])
            continue
        if u.get('standalone'):
            flush()
            cur.append(u)
            flush()
            continue
        if cur and sum(len(c['text'].s) for c in cur) + n > TARGET:
            flush()
        cur.append(u)
    flush()
    for k, p in enumerate(out):
        p['ord'] = k
    return out, headings


def _text(raw, u):
    if u['kind'] == 'table':
        t = clean(raw, u['start'], u['end'])
        if u.get('header'):
            h = clean(u['header'])
            # the header row's characters aren't at this passage's offsets; it is context, mapped to the rows' start
            t = Mapped(h.s + '\n' + t.s, [u['start']] * (len(h.s) + 1) + t.pos)
        return t
    return clean(raw, u['start'], u['end'])


def _cut(m):
    """[(a, b)] pieces of a long Mapped text, at sentence boundaries, about TARGET
    long, each after the first starting one sentence back."""
    ss = sentences(m.s)
    if not ss:
        return [(0, len(m.s))]
    pieces, i = [], 0
    while i < len(ss):
        j, size = i, 0
        while j < len(ss) and (j == i or size + (ss[j][1] - ss[j][0]) <= TARGET):
            size += ss[j][1] - ss[j][0] + 1
            j += 1
        pieces.append((ss[i][0], ss[j - 1][1]))
        if j >= len(ss):
            break
        i = j - 1 if j - 1 > i else j          # one sentence of overlap
    return pieces
