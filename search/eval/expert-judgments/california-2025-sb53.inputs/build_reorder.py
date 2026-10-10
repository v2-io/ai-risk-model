import json,re,sys
R='/Users/josephwecker-v2/src/ai-risk-model'
G='/Users/josephwecker-v2/.claude/jobs/8c1808c5/tmp/gold'
W=R+'/.claude/worktrees/expert-sb53-gold/search/eval/expert-judgments'
t=open(R+'/ref/canonical/california-2025-sb53.md',encoding='utf-8').read()
L=lambda o:t.count('\n',0,int(o))+1
P={}
for r in open(G+'/passages.txt'):
    o,s,e,n=r.strip().split('|'); s,e=int(s),int(e)
    P[int(o)]=dict(lines=[L(s),L(e-1)],quote=' '.join(t[s:s+90].split())[:70])
J=json.load(open(W+'/california-2025-sb53.json'))
qs=list(J['queries'])
ideal=json.load(open('search/eval/expert-judgments/california-2025-sb53.inputs/ideal.json'))
notes=json.load(open('search/eval/expert-judgments/california-2025-sb53.inputs/notes.json'))
out=[]
for i,q in enumerate(qs):
    I=[(int(p),g) for p,g in ideal[q]['items']]; A=set(ideal[q].get('ok',[]))
    hy=json.loads(open(f'{G}/runs/{i:02d}.hybrid.json').read())['results']
    rank={int(x['passage'].split('#')[1]):x['rank'] for x in hy}
    items=[dict(passage=p,lines=P[p]['lines'],quote=P[p]['quote'],grade=g,shown_rank=rank.get(p)) for p,g in I]
    ids={p for p,_ in I}|A
    noise=[r for p,r in sorted(rank.items(),key=lambda x:x[1]) if p not in ids]
    e=dict(query=q,tool='hybrid',items=items,noise=noise)
    if notes.get(q,{}).get('hybrid'): e['note']=notes[q]['hybrid']
    out.append(e)
    txt=open(f'{G}/runs/{i:02d}.outline.txt').read()
    opened=[(int(a),int(b)) for a,b in re.findall(r'▸ L(\d+)–(\d+)',txt)]
    def cov(lr): return any(not(lr[1]<a or lr[0]>b) for a,b in opened)
    oitems=[dict(passage=p,lines=P[p]['lines'],quote=P[p]['quote'],grade=g,opened=cov(P[p]['lines'])) for p,g in I]
    good=[P[p]['lines'] for p in ids]
    onoise=[f'L{a}–{b}' for a,b in opened if not any(not(l[1]<a or l[0]>b) for l in good)]
    head=txt.split('\n')[1] if 'Nothing in scope' in txt.split('\n')[1] else None
    e=dict(query=q,tool='outline',items=oitems,noise=onoise,flagged_unanswered=bool(head),source_lines_in_opened_ranges=sum(b-a+1 for a,b in opened))
    if notes.get(q,{}).get('outline'): e['note']=notes[q]['outline']
    out.append(e)
meta=dict(key='california-2025-sb53',canonical_sha256=J['canonical_sha256'],repo_sha='f1c93eb0273e18dbb11ace23abe4f9b4ac4ad0de',
  judge=J['judge'],date='2026-10-10',
  commands=["bin/source-search hybrid -n 20 QUERY california-2025-sb53","bin/source-search outline QUERY california-2025-sb53 --lines 60 (--text read; JSON kept)"],
  how="Items are the tool's own passages (src.passages, ord), in the order they should have come, with the grade from stage 1 (the highest grade of any judged stretch inside the passage). shown_rank is the hybrid rank, null if not in the top 20. For the outline, 'opened' says whether any opened range overlaps the passage, since the outline has no ranks. 'noise' lists hybrid ranks, or outline ranges, holding no graded passage; passages that are relevant but weren't graded (listed per query as acceptable) aren't counted as noise.",
  passages={str(k):v['lines'] for k,v in P.items()})
json.dump(dict(meta=meta,entries=out),open(W+'/california-2025-sb53.reorder.json','w'),indent=1,ensure_ascii=False)
for e in out:
    if e['tool']=='hybrid':
        print(e['query'][:40],'| items',[(x['passage'],x['grade'],x['shown_rank']) for x in e['items']],'| noise',e['noise'])
    else:
        print('   outline: missed',[x['passage'] for x in e['items'] if not x['opened']],'| noise',e['noise'],'| unans',e['flagged_unanswered'],e['opened_lines'])
