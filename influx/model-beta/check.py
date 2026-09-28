#!/usr/bin/env python3
"""Validate the model and print loops plus each relation's standing, as read off its claims.

Usage: python3 model/check.py [--standing] [--loops] [--all-loops]

Loop enumeration is opt-in: with all shards loaded it runs to hundreds of thousands of cycles and takes minutes.
"""
import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).parent
def load(prefix):
    """Load `prefix.yaml` plus any shards `prefix-<slice>.yaml`, so agents can work in parallel."""
    items = []
    for f in sorted(HERE.glob(f"{prefix}*.yaml")):
        items += yaml.safe_load(f.read_text()) or []
    return items

concepts, mappings, relations = load("concepts"), load("mappings"), load("relations")
for kind, items in (("concept", concepts), ("relation", relations)):
    seen = set()
    for it in items:
        if it["id"] in seen:
            print(f"ERROR: duplicate {kind} id {it['id']}"); sys.exit(1)
        seen.add(it["id"])

cids = {c["id"] for c in concepts}
rids = {r["id"] for r in relations}
errors = []

for c in concepts:
    for b in c.get("broader", []) or []:
        if b not in cids:
            errors.append(f"concept {c['id']}: broader {b} unknown")
    for d in c.get("distinct_from", []) or []:
        if d not in cids:
            errors.append(f"concept {c['id']}: distinct_from {d} unknown")
for m in mappings:
    if m["concept"] not in cids:
        errors.append(f"mapping {m['term']!r}: concept {m['concept']} unknown")
for r in relations:
    if r["from"] not in cids:
        errors.append(f"{r['id']}: from {r['from']} unknown")
    if r["type"] == "moderates":
        for t in r.get("targets", []):
            if t not in rids:
                errors.append(f"{r['id']}: target {t} unknown")
    elif r.get("to") not in cids:
        errors.append(f"{r['id']}: to {r.get('to')} unknown")
    if not r.get("claims"):
        errors.append(f"{r['id']}: no claims")

if errors:
    print("ERRORS"); print("\n".join(errors)); sys.exit(1)

kinds = defaultdict(int)
for c in concepts:
    kinds[c["kind"]] += 1
types = defaultdict(int)
for r in relations:
    types[r["type"]] += 1
nclaims = sum(len(r["claims"]) for r in relations)
print(f"{len(concepts)} concepts {dict(kinds)}")
print(f"{len(mappings)} source-term mappings; {len(relations)} relations {dict(types)}; {nclaims} claims")

if "--loops" in sys.argv or "--all-loops" in sys.argv:
    # ---- loops over `influences` relations
    graph = defaultdict(list)
    rel_of = {}
    for r in relations:
        if r["type"] == "influences":
            graph[r["from"]].append((r["to"], r["sign"], r["id"]))

    cycles = {}
    def dfs(start, node, path, signs, rids):
        for nxt, s, rid in graph.get(node, []):
            if nxt == start:
                cyc = tuple(path); k = cyc.index(min(cyc))
                cycles.setdefault(cyc[k:] + cyc[:k], (signs + [s], rids + [rid]))
            elif nxt not in path and nxt > start:
                dfs(start, nxt, path + [nxt], signs + [s], rids + [rid])
    for n in sorted(graph):
        dfs(n, n, [n], [], [])

    def loop_kind(signs):
        if any(s == "?" for s in signs):
            return "?"
        return "B" if sum(s.startswith("-") for s in signs) % 2 else "R"

    _ours = ("Joseph", "integrator", "prior Claude agent")
    rmap = {r["id"]: r for r in relations}
    def firm(rid):
        """Firmly signed, and at least one claim from outside this project whose evidence bears on the link itself
        (not only on an endpoint or on a mechanism elsewhere)."""
        r = rmap[rid]
        return r["sign"] in ("+", "-") and any(
            not any(o in (c.get("author") or "") for o in _ours) and c.get("bears_on", "link") == "link"
            for c in r["claims"])

    firm_loops = {c: v for c, v in cycles.items() if all(firm(x) for x in v[1])}
    per_rel = defaultdict(int)
    for _, (_, rids) in cycles.items():
        for x in rids:
            per_rel[x] += 1
    kinds = defaultdict(int)
    for _, (signs, _) in cycles.items():
        kinds[loop_kind(signs)] += 1
    print(f"\n{len(cycles)} loops {dict(kinds)}. {len(firm_loops)} close using only outside-supported, firmly signed links:")
    for cyc, (signs, _) in sorted(firm_loops.items(), key=lambda x: len(x[0])):
        print(f"  {loop_kind(signs)}  {' → '.join(cyc)} → {cyc[0]}")
    print("\nRelations appearing in the most loops: the load-bearing ones. Sensitivity, not verdict: each is a place where much structure rests on one claim-set.")
    for rid, n in sorted(per_rel.items(), key=lambda x: -x[1])[:10]:
        r = rmap[rid]
        status = ("sign unsettled" if r["sign"] not in ("+", "-") else
                  "outside-supported" if firm(rid) else "this project's premise/hypothesis only")
        print(f"  {n:5}  {rid:28} {r['sign']:3} {status}")
    if "--all-loops" in sys.argv:
        print("\nAll loops:")
        for cyc, (signs, _) in sorted(cycles.items(), key=lambda x: len(x[0])):
            print(f"  {loop_kind(signs)}  {' → '.join(cyc)} → {cyc[0]}   {signs}")


if "--standing" in sys.argv:
    # Standing is DESCRIBED, never scored: "strong" is deliberately undefined (a risk model weighs harm too).
    clusters = yaml.safe_load((HERE / "authors.yaml").read_text())
    def cluster(author):
        for cid, keys in clusters.items():
            if any(k in (author or "") for k in keys):
                return cid
        return author
    order = ["none-stated", "definition", "instrument", "argument", "expert-judgment", "established-practice", "document-change", "measurement", "incident"]
    rank = lambda e: order.index(e) if e in order else -1
    cmap = {c["id"]: c for c in concepts}
    ours = lambda cid: any(k in (cmap[cid].get("proposed_by") or "") for k in ("integrator", "Joseph", "prior agent"))
    print("\nRelation standing. Columns: sign · claims · independent author clusters · strongest evidence on the LINK"
          " (endpoint-only evidence in brackets) · target scale. '*' = concept proposed only within this project.")
    for r in relations:
        cl = r["claims"]
        cls = {cluster(c.get("author")) for c in cl}
        link = [c.get("evidence", "none-stated") for c in cl if c.get("bears_on", "link") == "link"]
        endp = [c.get("evidence", "none-stated") for c in cl if c.get("bears_on", "link") != "link"]
        ev = max(link, key=rank) if link else "—"
        if endp:
            ev += f" [{max(endp, key=rank)}]"
        tgt = r.get("to") or ",".join(r.get("targets", []))
        mark = lambda x: x + ("*" if x in cmap and ours(x) else "")
        scale = cmap.get(r.get("to"), {}).get("scale", "")
        only_us = "  (this project only)" if cls == {"this-project"} else ""
        print(f"  {r['id']:24} {str(r.get('sign','')):3} {len(cl)} · {len(cls)} · {ev:32} {mark(r['from'])} → {mark(tgt)}"
              + (f"   [{scale}]" if scale else "") + only_us)
