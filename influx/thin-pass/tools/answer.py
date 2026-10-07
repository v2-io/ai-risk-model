#!/usr/bin/env python3
"""Compute Q1's answer from the thin pass's records, so it is not hand-maintained.

    python3 -I tools/answer.py            print the answer and weights
    python3 -I tools/answer.py --write    also rewrite the generated block in answer.md

For each scenario (records/scenarios.yaml), each date, and each frame that
classifies a risk, a harm or an occurrence, it evaluates the frame's test in
three-valued logic and reports:
  - the result: yes / no / open;
  - the facts still open (only those that could change the result);
  - each ambiguity met on the way, and whether choosing among its candidates
    changed the result (decisive) or not (moot).
Then it computes lineage drift by diffing frames slot by slot, checks xAI's
quotation of SB 53 against SB 53's own words, and counts the independent
lineages of the bar. Disposable, like everything in this directory.
"""
import re
import sys
import copy
import pathlib
import datetime

import yaml

HERE = pathlib.Path(__file__).resolve().parent.parent
INF = float("inf")
T, F, U = "yes", "no", "open"


def load():
    return {p.stem: yaml.safe_load(p.read_text()) for p in sorted((HERE / "records").glob("*.yaml"))}


# ------------------------------------------------------------ frames
def resolve_frames(tr):
    raw = {f["id"]: f for f in tr["frames"]}
    out = {}

    def get(fid):
        if fid in out:
            return out[fid]
        f = copy.deepcopy(raw[fid])
        if "inherit" in f:
            parent = get(f["inherit"])
            merged = copy.deepcopy(parent)
            slots = {s["key"]: s for s in merged["slots"]}
            for o in f.get("override", []):
                base = slots.get(o["key"], {})
                new = {**base, **o}
                slots[o["key"]] = new
            merged["slots"] = list(slots.values())
            subst = f.get("substitute_frames", {})
            if subst:
                merged["slots"] = yaml.safe_load(
                    re.sub("|".join(map(re.escape, subst)), lambda m: subst[m.group(0)],
                           yaml.safe_dump(merged["slots"], sort_keys=False)))
            for k, v in f.items():
                if k not in ("inherit", "override", "slots", "substitute_frames"):
                    merged[k] = v
            merged["id"] = fid
            merged["inherited_from"] = f["inherit"]
            f = merged
        out[fid] = f
        return f

    for fid in raw:
        get(fid)
    return out


# ------------------------------------------------------------ evaluation
class Ctx:
    def __init__(self, facts, frames, force=None, closed=False):
        self.facts, self.frames, self.closed = facts, frames, closed
        self.force = force or {}  # R-id -> the one candidate to evaluate
        self.ambig = {}          # R-id -> {"status": node-level "decisive"|"moot", "values": candidate->value}

    def num(self, name):
        v = self.facts.get(name)
        return (0.0, INF) if v is None else (float(v), float(v))


def kleene_all(vals):
    if any(v == F for v in vals):
        return F
    return T if all(v == T for v in vals) else U


def kleene_any(vals):
    if any(v == T for v in vals):
        return T
    return F if all(v == F for v in vals) else U


def ev(t, c, where):
    """Return (value, open_facts). open_facts can change the value."""
    if isinstance(t, dict) and "test" in t and "key" in t:      # a slot
        return ev(t["test"], c, t["key"])
    lab = t.get("label") if isinstance(t, dict) else None
    if "fact" in t:
        if t.get("genus") and c.closed:      # closure probe: read the open class as closed
            return F, set()
        v = c.facts.get(t["fact"])
        if v is None:
            return U, {f"{where}: {t['fact']}"}
        return (T if v else F), set()
    if "fact_in" in t:
        name, vals = t["fact_in"]
        v = c.facts.get(name)
        if v is None:
            return U, {f"{where}: {name} in {vals}"}
        return (T if v in vals else F), set()
    if "cmp" in t:
        expr, op, n = t["cmp"]
        if isinstance(expr, dict):
            lo = sum(c.num(x)[0] for x in expr["sum"])
            hi = sum(c.num(x)[1] for x in expr["sum"])
            names = expr["sum"]
        else:
            lo, hi = c.num(expr)
            names = [expr]
        if op == ">":
            v = T if lo > n else (F if hi <= n else U)
        elif op == ">=":
            v = T if lo >= n else (F if hi < n else U)
        else:
            raise ValueError(op)
        return v, ({f"{where}: {'+'.join(names)} {op} {n:g}"} if v == U else set())
    if "not" in t:
        v, o = ev(t["not"], c, where)
        return {T: F, F: T, U: U}[v], o
    if "all" in t or "any" in t:
        kids = [ev(k, c, where) for k in (t["all"] if "all" in t else t["any"])]
        vals = [k[0] for k in kids]
        v = kleene_all(vals) if "all" in t else kleene_any(vals)
        o = set().union(*[k[1] for k in kids if k[0] == U]) if v == U else set()
        return v, o
    if "frame" in t:
        return eval_frame(c.frames[t["frame"]], c)
    if "ambiguous" in t:
        rid = t["ambiguous"]
        if rid in c.force:
            c.ambig.setdefault(rid, {"status": "forced", "values": {}})
            return ev(t["candidates"][c.force[rid]], c, where)
        res = {name: ev(cand, c, where) for name, cand in t["candidates"].items()}
        vals = {name: r[0] for name, r in res.items()}
        same = len(set(vals.values())) == 1
        prev = c.ambig.get(rid)
        status = "moot" if same else "decisive"
        if prev and prev["status"] == "decisive":
            status = "decisive"
        c.ambig[rid] = {"status": status, "values": vals}
        o = set().union(*[r[1] for r in res.values()])
        return (next(iter(vals.values())) if same else U), (o if not same or next(iter(vals.values())) == U else set())
    raise ValueError(f"unknown test {t}")


def eval_frame(f, c):
    vals = [ev(s, c, s["key"]) for s in f["slots"]]
    v = kleene_all([x[0] for x in vals])
    o = set().union(*[x[1] for x in vals if x[0] == U]) if v == U else set()
    return v, o


def in_force(f, date):
    inf = f.get("in_force") or {}
    fr, to = inf.get("from"), inf.get("to")
    if fr is None:
        return "in force (start not recorded)"
    if inf.get("end") == "undetermined" and str(date) >= str(fr):
        return "in force from its date; end undetermined"
    fr = str(fr)
    if len(fr) == 4:
        fr = fr + "-01-01"
    d = str(date)
    if d < fr:
        return "not yet in force"
    if to and d >= str(to):
        return "superseded"
    return "in force"


# ------------------------------------------------------------ lineage
def norm(s):
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def lineage(rec, frames):
    out = []
    edges = rec["lineage"]["records"]
    bar_frames = {"F-sb53-bp-cr", "F-sb53-lab-cr", "F-raise-cr", "F-xai25-cr", "F-fcf-own", "F-fgf-own"}
    out.append("Drift, computed slot by slot from the frames (words that differ):")
    for e in edges:
        a, b = e.get("from"), e.get("to")
        if not (a and isinstance(b, str)) or a not in frames or b not in frames:
            continue
        fa, fb = frames[a], frames[b]
        if not any(x in ("all", "bar") for x in (e.get("carries") or [])):
            out.append(f"  {e['id']}: {a} -> {b}: carries nothing of the bar (a document revision); not diffed")
            continue
        sa = {s["key"]: s for s in fa["slots"]}
        sb = {s["key"]: s for s in fb["slots"]}
        diffs = []
        for k in sorted(set(sa) | set(sb)):
            if k not in sb:
                diffs.append(f"{k}: dropped")
            elif k not in sa:
                diffs.append(f"{k}: added")
            else:
                w = norm(str(sa[k].get("words"))) != norm(str(sb[k].get("words")))
                t = sa[k].get("test") != sb[k].get("test")
                if w or t:
                    diffs.append(f"{k}: " + {(True, True): "words and test differ", (True, False): "words differ, same test",
                                             (False, True): "SAME WORDS, different test"}[(w, t)])
        note = "; ".join(diffs) if diffs else "no slot differs"
        if [s_["key"] for s_ in fb.get("slots", [])] == ["incorporated"] and "incorporation" in e["relation"]:
            note = "incorporation by reference: the later frame is the earlier one (checked below)"
        out.append(f"  {e['id']}: {a} -> {b}: {note}")

    # xAI's quotation of SB 53, word for word
    ps = {p["id"]: p for p in rec["passages"]["passages"]}
    q_x = norm(ps["P-xai25-fn"]["quote"]).split('"', 1)[1]
    q_s = norm(ps["P-sb53-bp-cr"]["quote"]).split("means ", 1)[1]
    out.append(f"  L-xai25-quote: xAI's quotation equals SB 53 §22757.11(c)(1)'s head: {q_x == q_s}")
    c_x = norm(ps["P-xai25-fn-conducts"]["quote"]).rstrip('"')
    c_s = norm(ps["P-sb53-bp-cr-conducts"]["quote"])
    out.append(f"  L-xai25-quote: and its (A)-(C) equal SB 53's: {c_x == c_s}. The footnote does not quote the exclusions in (c)(2).")

    # Independent lineages of the bar: roots among bar-carrying frames.
    carried = [e for e in edges if isinstance(e.get("to"), str) and e.get("from") in bar_frames and e.get("to") in bar_frames
               and any(x in ("all", "bar") for x in (e.get("carries") or []))]
    has_parent = {e["to"] for e in carried}
    roots = sorted(bar_frames - has_parent)
    upstream = [e for e in edges if e.get("from") is None and isinstance(e.get("to"), str) and e.get("to") in roots and e["relation"] == "undetermined"]
    out.append("")
    out.append(f"Frames carrying the >50 / $1B single-incident bar: {len(bar_frames)} "
               f"in {len({f.split('-')[1] for f in bar_frames})} documents.")
    out.append(f"Roots (independent lineages) within the slice: {len(roots)}: {', '.join(roots)}")
    for e in upstream:
        out.append(f"  upstream of {e['to']}: undetermined ({e['id']})")
    for e in edges:
        if e.get("not_independent_of"):
            out.append(f"  {e['id']} is not independent of {e['not_independent_of']}: shared wording beyond SB 53 (see that record)")
    return out


# ------------------------------------------------------------ report
WHAT = [
    ("F-sb53-bp-cr", "SB 53 B&P §22757.11(c)", "catastrophic risk", "risk"),
    ("F-sb53-lab-cr", "SB 53 Labor Code §1107(a)", "catastrophic risk", "risk"),
    ("F-sb53-bp-csi", "SB 53 B&P §22757.11(d)", "critical safety incident", "occurrence"),
    ("F-sb53-lab-csi", "SB 53 Labor Code §1107(c)", "critical safety incident", "occurrence"),
    ("F-raise-cr", "RAISE S.8828 §1420(3) (as introduced)", "catastrophic risk", "risk"),
    ("F-raise-csi", "RAISE S.8828 §1420(4) (as introduced)", "critical safety incident", "occurrence"),
    ("F-xai25-cr", "xAI FAIF 2025", "Catastrophic Risk (TFAIA's)", "risk"),
    ("F-xairmf-cme", "xAI RMF 2025", "catastrophic malicious use events", "occurrence"),
    ("F-fcf-systemic", "Anthropic FCF v2", "systemic risk", "risk"),
    ("F-fcf-own", "Anthropic FCF v2, its own sentence", "systemic risk (P-fcf-def)", "risk"),
    ("F-fgf-systemic", "OpenAI FGF", "systemic risk", "risk"),
    ("F-fgf-own", "OpenAI FGF, its own sentence", "systemic risk (P-fgf-def)", "risk"),
    ("F-eu-systemic", "EU AI Act Art. 3(65)", "systemic risk", "risk"),
    ("F-fgf-severe", "OpenAI FGF", "severe harm", "harm"),
    ("F-pf-severe", "OpenAI PF v2", "severe harm", "harm"),
]


def candidate_names(tr, rid):
    names = []
    def walk(x):
        if isinstance(x, dict):
            if x.get("ambiguous") == rid:
                for n in x["candidates"]:
                    if n not in names:
                        names.append(n)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(tr["frames"])
    return names


def report(rec):
    frames = resolve_frames(rec["translation"])
    res = {r["id"]: r for r in rec["resolutions"]["records"]}
    lines, weights, opens_by = [], {}, {}
    for sc in rec["scenarios"]["scenarios"]:
        lines.append(f"### Scenario `{sc['id']}`: {sc['question']}")
        lines.append("")
        lines.append("| Document | Its term | Classifies | Result under our frame (unreviewed) | Still open (facts that could change it) | Ambiguities met, and whether choosing changes this row |")
        lines.append("|---|---|---|---|---|---|")
        for fid, doc, term, kind in WHAT:
            c = Ctx(dict(sc["facts"]), frames)
            v, o = eval_frame(frames[fid], c)
            for rid in list(c.ambig):
                names = candidate_names(rec["translation"], rid)
                rowvals = {n: eval_frame(frames[fid], Ctx(dict(sc["facts"]), frames, {rid: n}))[0] for n in names}
                c.ambig[rid]["row"] = rowvals
                c.ambig[rid]["row_decisive"] = len(set(rowvals.values())) > 1
            v_closed = eval_frame(frames[fid], Ctx(dict(sc["facts"]), frames, closed=True))[0]
            if v_closed != v:
                amb_closure = f"**closure decides this row** (as written: {v}; read as closed: {v_closed})"
            else:
                amb_closure = None
            opens = "<br>".join(sorted(o)) if o else "none"
            for x in o:
                fact = x.split(": ", 1)[1].split(" ")[0]
                opens_by.setdefault(fact, {}).setdefault(sc["id"], set()).add(fid)
            amb = []
            for rid, a in sorted(c.ambig.items()):
                status = "row" if a["row_decisive"] else ("clause" if a["status"] == "decisive" else "moot")
                weights.setdefault(sc["id"], {}).setdefault(rid, []).append(status)
                pref = res.get(rid, {}).get("our_preference")
                if status == "row":
                    vs = ", ".join(f"{k}: {x}" for k, x in a["row"].items())
                    amb.append(f"**{rid} decides this row** ({vs}{'; our lean: ' + pref if pref else ''})")
                elif status == "clause":
                    amb.append(f"{rid} decides its clause only; the row stays {v}")
                else:
                    amb.append(f"{rid} moot")
            if amb_closure:
                amb.append(amb_closure)
                weights.setdefault(sc["id"], {}).setdefault("closure (open bars)", []).append("row")
            lines.append(f"| {doc} | {term} | {kind} | **{v}** | {opens} | {'<br>'.join(amb) or 'none'} |")
        lines.append("")
    lines.append("### In force on which date (Q1 gives none)")
    lines.append("")
    dates = rec["scenarios"]["dates"]
    lines.append("| Frame | " + " | ".join(str(d) for d in dates) + " |")
    lines.append("|---|" + "---|" * len(dates))
    for fid, doc, term, kind in WHAT:
        lines.append(f"| {doc}: {term} | " + " | ".join(in_force(frames[fid], d) for d in dates) + " |")
    lines.append("")
    lines.append("### Lineage")
    lines.append("")
    lines.append("```")
    lines.extend(lineage(rec, frames))
    lines.append("```")
    lines.append("")
    lines.append("### Ambiguity weight across scenarios (computed at the row)")
    lines.append("")
    lines.append("Each cell: rows where choosing a reading changes the row's result / rows where it changes only its own clause / rows where the ambiguity is reached at all. Only ambiguities encoded as `ambiguous:` nodes can appear here.")
    lines.append("")
    rids = sorted({r for s in weights.values() for r in s})
    lines.append("| Resolution record | " + " | ".join(f"`{s}`" for s in weights) + " |")
    lines.append("|---|" + "---|" * len(weights))
    for r in rids:
        cells = []
        for s_ in weights:
            st = weights[s_].get(r, [])
            cells.append(f"{st.count('row')} / {st.count('clause')} / {len(st)}" if st else "not reached")
        lines.append(f"| {r} | " + " | ".join(cells) + " |")
    lines.append("")
    enc = {m for m in re.findall(r"ambiguous: (R-[a-z0-9-]+)", (HERE / 'records' / 'translation.yaml').read_text())}
    unenc = [r["id"] for r in rec["resolutions"]["records"] if r.get("candidates") and r["id"] not in enc]
    deleg = [r["id"] for r in rec["resolutions"]["records"] if r.get("status") == "delegated"]
    lines.append("Not evaluable, so absent from this table by construction: resolution records with candidates that no test encodes ("
                 + ", ".join(unenc) + "), and delegated records with no candidates (" + ", ".join(deleg) + ").")
    lines.append("")
    lines.append("### Facts left open (computed): in how many of the rows above each could still change the result")
    lines.append("")
    scs = [sc["id"] for sc in rec["scenarios"]["scenarios"]]
    lines.append("| Fact | " + " | ".join(f"`{x}`" for x in scs) + " |")
    lines.append("|---|" + "---|" * len(scs))
    for fact in sorted(opens_by, key=lambda f: (-sum(len(v) for v in opens_by[f].values()), f)):
        lines.append(f"| {fact} | " + " | ".join(str(len(opens_by[fact].get(x, ()))) for x in scs) + " |")
    return lines


def main():
    rec = load()
    lines = report(rec)
    text = "\n".join(lines)
    print(text)
    if "--write" in sys.argv:
        p = HERE / "answer.md"
        s = p.read_text()
        start, end = "<!-- BEGIN generated by tools/answer.py; do not edit by hand -->", "<!-- END generated -->"
        a, b = s.index(start) + len(start), s.index(end)
        p.write_text(s[:a] + "\n\n" + text + "\n\n" + s[b:])
        print("\nwrote answer.md", file=sys.stderr)


if __name__ == "__main__":
    main()
