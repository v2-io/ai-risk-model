#!/usr/bin/env python3
"""Build the "Aligned to whom?" map from a small markdown file.

    python3 build.py                          # alignment.md -> alignment.html
    python3 build.py other.md -o other.html
    python3 build.py --link                   # link the CSS / JS instead of inlining (edit CSS, just reload)
    python3 build.py --palette                # also write palette.html (every colour class)

Standard library only. Structure lives in template.html, layout in style.css and
all colour in palette.css; the connector
lines are drawn in the browser by lines.js from the rendered boxes, so rows and
boxes can change size freely and the lines follow.

Markdown format (see alignment.md):
  optional front matter   key: value lines between --- fences
  # Title
  paragraphs              intro; a paragraph starting with ">" becomes the lead
  ## Stack                table: id | layer | gloss | class | group | parent | size
  ## Actors               table: display columns... | edges | class
  ## Notes                paragraphs shown under the table (optional)
  ## Footnote             paragraphs shown under the stack (optional)
"""
import argparse
import html
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


# ---------------------------------------------------------------- markdown bits

def inline(text):
    """Escape HTML, then apply a small subset of inline markdown."""
    t = html.escape(text.strip(), quote=False)
    t = re.sub(r"\\([\\*_`|>#-])", lambda m: "\x00%d\x00" % ord(m.group(1)), t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(?<![\w_])_(?!\s)(.+?)(?<!\s)_(?![\w_])", r"<em>\1</em>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", r'<a href="\2">\1</a>', t)
    return re.sub(r"\x00(\d+)\x00", lambda m: chr(int(m.group(1))), t)


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", s)]


def parse_table(lines):
    rows = [l for l in lines if l.strip().startswith("|")]
    if len(rows) < 2:
        return [], []
    header = split_row(rows[0])
    body = [split_row(r) for r in rows[2:]]
    body = [r + [""] * (len(header) - len(r)) for r in body]
    return header, body


def paragraphs(lines):
    out, cur = [], []
    for l in lines + [""]:
        if l.strip() == "" or l.strip().startswith("|"):
            if cur:
                out.append(" ".join(s.strip() for s in cur))
                cur = []
        else:
            cur.append(l)
    return out


def parse(md):
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    lines = md.splitlines()
    meta = {}
    if lines and lines[0].strip() == "---":
        end = lines.index("---", 1)
        for l in lines[1:end]:
            if ":" in l:
                k, v = l.split(":", 1)
                meta[k.strip()] = v.strip()
        lines = lines[end + 1:]
    title, sections, name = "", {"_intro": []}, "_intro"
    for l in lines:
        if l.startswith("# ") and not title:
            title = l[2:].strip()
        elif l.startswith("## "):
            name = l[3:].strip().lower()
            sections[name] = []
        else:
            sections[name].append(l)
    return meta, title, sections


# ---------------------------------------------------------------- rendering

def render_intro(lines):
    out = []
    for p in paragraphs(lines):
        if p.startswith(">"):
            out.append('<p class="lead">%s</p>' % inline(p.lstrip("> ")))
        else:
            out.append('<p class="intro">%s</p>' % inline(p))
    return "\n".join(out)


def render_stack(lines):
    header, body = parse_table(lines)
    col = {h.lower(): i for i, h in enumerate(header)}
    get = lambda r, k: r[col[k]] if k in col else ""
    items = [dict(id=get(r, "id"), layer=get(r, "layer"), gloss=get(r, "gloss"),
                  cls=get(r, "class"), group=get(r, "group"), parent=get(r, "parent"),
                  size=get(r, "size")) for r in body]
    ids = {i["id"] for i in items}
    for i in items:
        if i["parent"] and i["parent"] not in ids:
            sys.exit("stack: unknown parent %r for %r" % (i["parent"], i["id"]))

    def box(i, grow=True):
        kids = "".join(box(k, False) for k in items if k["parent"] == i["id"])
        style = ' style="flex-grow: %s"' % i["size"] if grow and i["size"] else ""
        return ('<div class="layer %s" data-layer="%s"%s><div class="layer-head">'
                '<span class="name">%s</span><span class="gloss">%s</span></div>%s</div>'
                % (html.escape(i["cls"]), html.escape(i["id"]), style,
                   inline(i["layer"]), inline(i["gloss"]), kids))

    out, top, n = [], [i for i in items if not i["parent"]], 0
    while n < len(top):
        g = top[n]["group"]
        if g:
            members = []
            while n < len(top) and top[n]["group"] == g:
                members.append(top[n])
                n += 1
            size = sum(float(m["size"] or 1) for m in members)
            out.append('<div class="group %s %s" style="flex-grow: %g">%s</div>'
                       % (html.escape(g), html.escape(members[0]["cls"]), size,
                          "".join(box(m) for m in members)))
        else:
            out.append(box(top[n]))
            n += 1
    return "\n".join(out), ids


def render_actors(lines, stack_ids):
    header, body = parse_table(lines)
    lower = [h.lower() for h in header]
    ei = lower.index("edges") if "edges" in lower else None
    ci = lower.index("class") if "class" in lower else None
    shown = [i for i in range(len(header)) if i not in (ei, ci)]
    head = "".join("<span>%s</span>" % inline(header[i]) for i in shown)
    main, ref = [], []
    for r in body:
        cls = r[ci].strip() if ci is not None else ""
        edges = []
        if ei is not None:
            for e in filter(None, (x.strip() for x in r[ei].split(","))):
                tid, _, w = e.partition(":")
                tid = tid.strip()
                if tid not in stack_ids:
                    sys.exit("actor %r: unknown edge target %r (stack ids: %s)"
                             % (r[0], tid, ", ".join(sorted(stack_ids))))
                edges.append("%s:%s" % (tid, (w.strip() or "1")))
        cells = "".join(('<b>%s</b>' if k == 0 else "<span>%s</span>") % inline(r[i])
                        for k, i in enumerate(shown))
        row = '<div class="row %s" data-edges="%s">%s</div>' % (
            html.escape(cls), " ".join(edges), cells)
        (ref if "referent" in cls.split() else main).append(row)
    return head, len(shown), "\n".join(main), "\n".join(ref)


CSS = ("palette.css", "style.css")


def styles(link):
    if link:
        return "\n".join('<link rel="stylesheet" href="%s">' % f for f in CSS)
    return "<style>\n%s\n</style>" % "\n\n".join((HERE / f).read_text(encoding="utf-8") for f in CSS)


def build(md_path, out_path, link):
    meta, title, sec = parse(Path(md_path).read_text(encoding="utf-8"))
    stack_html, ids = render_stack(sec.get("stack", []))
    head, ncols, rows, refs = render_actors(sec.get("actors", []), ids)
    para = lambda k, c: "\n".join('<p class="%s">%s</p>' % (c, inline(p))
                                  for p in paragraphs(sec.get(k, [])))
    script = ('<script src="lines.js"></script>' if link else
              "<script>\n%s\n</script>" % (HERE / "lines.js").read_text(encoding="utf-8"))
    slots = {
        "title": inline(title), "title_text": html.escape(title),
        "kicker_left": inline(meta.get("kicker_left", "")),
        "kicker_right": inline(meta.get("kicker_right", "")),
        "stack_label": inline(meta.get("stack_label", "")),
        "intro": render_intro(sec.get("_intro", [])),
        "head": head, "ncols": str(ncols - 1),
        "rows": rows, "referents": refs, "stack": stack_html,
        "notes": para("notes", "note"), "footnote": para("footnote", "footnote"),
        "style": styles(link), "script": script,
    }
    page = (HERE / "template.html").read_text(encoding="utf-8")
    page = re.sub(r"\{\{(\w+)\}\}", lambda m: slots.get(m.group(1), m.group(0)), page)
    Path(out_path).write_text(page, encoding="utf-8")
    print("wrote %s" % out_path)


def build_palette(out_path):
    """Swatch page for every colour family in palette.css (links the CSS, so it stays current)."""
    css = (HERE / "palette.css").read_text(encoding="utf-8")
    families = list(dict.fromkeys(re.findall(r"--([a-z]+)-deeper:\s*#", css)))
    blocks = []
    steps = (("", "normal"), ("deep", "deep"), ("deeper", "deeper"))
    for h in families:
        boxes = "".join(
            '<div class="layer %s %s"><div class="layer-head"><span class="name">%s</span>'
            '<span class="gloss">%s</span></div></div>' % (h, mod, (h + " " + mod).strip(), label)
            for mod, label in steps)
        rows = "".join(
            '<div class="row %s %s"><b>%s</b><span>%s</span></div>' % (
                h, mod, (h + " " + mod).strip(),
                'normal &nbsp;·&nbsp; <b class="ink">%s accent</b> <i>name in the family\u2019s ink</i>' % h
                if not mod else label)
            for mod, label in steps)
        blocks.append('<section class="swatch %s"><div class="rows">%s</div>'
                      '<svg viewBox="0 0 120 56"><path class="w1" d="M0,14 C60,14 60,22 120,22"/>'
                      '<path class="w3" d="M0,44 C60,44 60,36 120,36"/></svg>'
                      '<div class="boxes">%s</div></section>' % (h, rows, boxes))
    page = """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Palette</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;1,6..72,400&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono&display=swap">
%s
<style>
.page{gap:14px} .swatch{display:grid;grid-template-columns:520px 120px 1fr;align-items:center}
.swatch .rows{--ncols:1} .swatch .row{min-height:36px;align-items:center}
.swatch .row b.ink{color:var(--accent)} .swatch .row i{color:var(--muted)}
.swatch svg{width:120px;height:56px;fill:none;stroke:var(--edge)} .swatch svg .w1{stroke-width:1.3;stroke-opacity:.65} .swatch svg .w3{stroke-width:3.2}
.boxes{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
</style></head><body><main class="page"><header class="masthead"><div class="kicker"><span>palette.css</span><span>colour families</span></div><h1>Palette</h1>
<p class="intro">Same classes on rows and boxes: <code>sand</code> (normal), <code>sand deep</code>, <code>sand deeper</code>; add <code>accent</code> for the name in the family\u2019s ink. Lines: weight 1 and weight 3.</p></header>
%s</main></body></html>""" % (styles(True), "\n".join(blocks))
    Path(out_path).write_text(page, encoding="utf-8")
    print("wrote %s" % out_path)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("markdown", nargs="?", default=str(HERE / "alignment.md"))
    ap.add_argument("-o", "--out")
    ap.add_argument("--link", action="store_true",
                    help="link palette.css, style.css and lines.js instead of inlining them")
    ap.add_argument("--palette", action="store_true",
                    help="also write palette.html showing every colour class")
    a = ap.parse_args()
    if a.palette:
        build_palette(str(HERE / "palette.html"))
    build(a.markdown, a.out or str(Path(a.markdown).with_suffix(".html")), a.link)
