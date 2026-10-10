"""Build versions/, diffs/, sections/, raw/ from the SB 53 CAML XML.
Usage (from history/):  python3 -I tools/build.py tools <dir> .
  <dir> holds either BILL_VERSION_TBL_<n>.lob files (from tools/fetch_pubinfo.py) or the raw/*.xml copies.
"""
import sys, os, re, subprocess, tempfile, html, xml.etree.ElementTree as ET
SCR, LOB, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, SCR)
from render import render, events
V = [ # (lob, versionNum, date, label, slug, how)
 (114, 99,'2025-01-07','Introduced','introduced','Introduced by Senator Wiener; referred to Senate Rules.'),
 (2523,98,'2025-02-27','Amended in Senate','amended-senate','"From committee with author\'s amendments. Read second time and amended. Re-referred to Com. on RLS."'),
 (3705,97,'2025-03-27','Amended in Senate','amended-senate','Senate G.O. "Do pass as amended" (Mar 25, 13-0); "Read second time and amended. Re-referred to Com. on JUD."'),
 (5602,96,'2025-05-23','Amended in Senate','amended-senate','Senate Appropriations "Do pass as amended" from suspense (May 23, 6-0). Passed Senate May 28 (37-0).'),
 (6563,95,'2025-07-08','Amended in Assembly','amended-assembly','Assembly: "From committee with author\'s amendments. Read second time and amended. Re-referred to Com. on P. & C.P." (after Asm JUD do-pass July 1, 12-0, on the May 23 text).'),
 (7139,94,'2025-07-17','Amended in Assembly','amended-assembly','Asm P.&C.P. "Do pass as amended" (July 16, 9-0); "Read second time and amended. Re-referred to Com. on APPR."'),
 (7772,93,'2025-09-02','Amended in Assembly','amended-assembly','Asm Appropriations "Do pass as amended" from suspense (Aug 29, 11-1); "Read second time and amended."'),
 (8050,92,'2025-09-05','Amended in Assembly','amended-assembly','Assembly floor: "Read third time and amended." Then re-referred to P.&C.P. under Asm Rule 77.2; do pass Sept 11 (12-1); passed Assembly Sept 12 (59-7); Senate concurred Sept 13 (29-8).'),
 (8894,91,'2025-09-17','Enrolled','enrolled','Enrolled; presented to the Governor Sept 23.'),
 (8965,90,'2025-09-29','Chaptered','chaptered','Approved by the Governor Sept 29; Chapter 138, Statutes of 2025.'),
]
def p(*a): return os.path.join(OUT,*a)
for d in ['versions','diffs','diffs/lc-marked','sections','raw']: os.makedirs(p(d),exist_ok=True)
names={}
xmls={}
for i,(lob,vn,date,label,slug,how) in enumerate(V,1):
    names[lob]=f'{i:02d}-{date}-{slug}'
    src=os.path.join(LOB,f'BILL_VERSION_TBL_{lob}.lob')
    if not os.path.exists(src): src=os.path.join(LOB,f'{names[lob]}.xml')   # e.g. LOB = ../raw
    xmls[lob]=open(src,encoding='utf-8').read()
HDR=lambda i,lob,vn,date,label,how,kind: (
 f'<!-- SB 53 (2025-2026), version {i:02d} of {len(V)}: {label}, {date}. {kind}\n'
 f'     Source: California Legislature, pubinfo_2025.zip (downloads.leginfo.legislature.ca.gov), BILL_VERSION_TBL,\n'
 f'     bill_version_id 20250SB53{vn}{ {99:"INT",91:"ENR",90:"CHP"}.get(vn,"AMD") }, file BILL_VERSION_TBL_{lob}.lob (Legislative Counsel CAML XML; copy in ../raw/).\n'
 f'     Legislative action: {how}\n'
 f'     Rendered by ../tools/render.py: one paragraph per <p>/heading element; EnSpace -> one space; whitespace collapsed.\n'
 f'     Nothing else is changed. Metadata elements (history, author list, digest key, chapter numbers) are not rendered. -->\n\n')
for i,(lob,vn,date,label,slug,how) in enumerate(V,1):
    n=names[lob]
    open(p('raw',f'{n}.xml'),'w',encoding='utf-8').write(xmls[lob])
    body='\n\n'.join(render(xmls[lob],'clean'))
    open(p('versions',f'{n}.md'),'w',encoding='utf-8').write(HDR(i,lob,vn,date,label,how,'Text as of this version (Legislative Counsel change marks applied).')+f'# SB 53 — {label}, {date}\n\n'+body+'\n')
    if i>1:
        has=('xm-insertion' in xmls[lob]) or ('xm-deletion' in xmls[lob])
        if has:
            mk='\n\n'.join(render(xmls[lob],'marked'))
            open(p('diffs','lc-marked',f'{n}.marked.txt'),'w',encoding='utf-8').write(
              HDR(i,lob,vn,date,label,how,"Legislative Counsel's OWN change marks against the previous version: {+inserted+} [-struck-]. (This is what leginfo prints as italic/strikeout.)")+mk+'\n')
# computed diffs
def gitdiff(a,b,word,ctx):
    args=['git','diff','--no-index','--no-color',f'-U{ctx}']
    if word: args+=['--word-diff=plain']
    r=subprocess.run(args+[a,b],capture_output=True,text=True)
    return r.stdout
def bodyfile(lob):
    f=tempfile.NamedTemporaryFile('w',delete=False,suffix='.txt',encoding='utf-8')
    f.write('\n'.join(render(xmls[lob],'clean'))+'\n'); f.close(); return f.name
for (a,*_),(b,*_) in zip(V,V[1:]):
    fa,fb=bodyfile(a),bodyfile(b)
    na,nb=names[a],names[b]
    tag=f'{na[:2]}-to-{nb[:2]}'
    hdr=f'# Computed diff (mine, not Legislative Counsel\'s): {na} -> {nb}\n# One line per paragraph. Produced with git diff --no-index on ../versions text bodies.\n'
    u=gitdiff(fa,fb,False,1); w=gitdiff(fa,fb,True,0)
    u,w=[x.replace(fa.lstrip('/'),na+'.txt').replace(fb.lstrip('/'),nb+'.txt') for x in (u,w)]
    if not u.strip(): u=w='(no textual difference)\n'
    open(p('diffs',f'{tag}.diff'),'w',encoding='utf-8').write(hdr+u)
    open(p('diffs',f'{tag}.word.diff'),'w',encoding='utf-8').write(hdr+'# Word-level: [-struck-] {+inserted+}\n'+w)
# section histories
NS={'caml':'http://lc.ca.gov/legalservices/schemas/caml.1#'}
CODE={'Business and Professions Code':'BPC','Government Code':'GOV','Labor Code':'LAB'}
def clean_xml(s):
    s=re.sub(r'<\?xm-deletion_mark data="[^"]*"\?>','',s); return re.sub(r'<\?xm-insertion_mark_(start|end)\?>','',s)
# Section numbers in the B&P chapter shifted between versions, so histories are keyed by
# LINEAGE (what the section does), not by number. The map below was built by reading the
# first line of every section in every version. Keys use the chaptered number where one exists.
def lineage(i, code, sn, first):
    if code=='BPC':
        if sn=='22757.10': return 'BPC-22757.10-short-title'
        if sn=='22757.11': return 'BPC-22757.11-definitions'
        if sn=='22757.12': return 'BPC-22757.12-protocol-framework-transparency'
        if sn=='22757.13': return 'BPC-22757.13-incident-reporting-and-whistleblower-reports'
        if (i==5 and sn=='22757.14') or (i==6 and sn=='22757.16') or (i>=7 and sn=='22757.15'): return 'BPC-22757.15-penalties'
        if (i in (5,6) and sn=='22757.15') or (i>=7 and sn=='22757.14'): return 'BPC-22757.14-definition-updates'
        if i==6 and sn=='22757.14': return 'BPC-x-third-party-audits-(v06-only)'
        if i>=8 and sn=='22757.16': return 'BPC-22757.16-equity-not-property'
        raise SystemExit(f'unmapped BPC {i} {sn} {first[:60]}')
    if code=='GOV': return 'GOV-11546.8-calcompute'   # was 11547.6.1 in versions 02-04
    if code=='LAB': return {'1107':'LAB-1107-definitions','1107.1':'LAB-1107.1-whistleblower-protections','1107.2':'LAB-1107.2-equity-not-property'}[sn]
def units(i, lob):
    root=ET.fromstring(clean_xml(xmls[lob]).encode()); out={}
    for bs in root.iter('{%s}BillSection'%NS['caml']):
        num=' '.join(''.join(bs.find('caml:Num',NS).itertext()).split())
        al=bs.find('caml:ActionLine',NS)
        lss=list(bs.iter('{%s}LawSection'%NS['caml']))
        if lss:
            code=CODE[' '.join(''.join(al.find('caml:DocName',NS).itertext()).split())]
            for ls in lss:
                sn=' '.join(''.join(ls.find('caml:Num',NS).itertext()).split()).rstrip('.')
                t=render(ET.tostring(ls,encoding='unicode'),'clean')
                out[lineage(i,code,sn,' '.join(t[1:2]))]=(f'{code} §{sn}',t)
        else:
            t=render(ET.tostring(bs,encoding='unicode'),'clean')
            if i==1: key='bill-SEC1-intent-(introduced-only)'
            elif num in('SECTION 1.',): key='bill-SEC1-findings'
            elif num=='SEC. 5.': key='bill-SEC5-construction-and-scope'
            elif num=='SEC. 6.': key='bill-SEC6-public-access-findings'
            else: raise SystemExit('unmapped bill section '+num)
            out[key]=(num,t)
    d=root.find('.//caml:DigestText',NS)
    out['digest']=("Legislative Counsel's Digest",render(ET.tostring(d,encoding='unicode'),'clean'))
    return out
U={lob:units(i,lob) for i,(lob,*_) in enumerate(V,1)}
keys=[]
for lob,*_ in V:
    for k in U[lob]:
        if k not in keys: keys.append(k)
for k in keys:
    lines=[f'# {k} — across the versions of SB 53\n\n',
      '<!-- Computed by ../tools/build.py from the version texts (mine, not Legislative Counsel\'s marks; see ../diffs/lc-marked/ for those).\n     Keyed by LINEAGE, not number: the section numbers in the B&P chapter shifted (see "Numbered as" below).\n     "Changes" blocks are git word-diffs against the previous version that has this section: [-struck-] {+inserted+}. Full text, not just hunks. -->\n\n']
    pres=[(lob,date,label) for lob,vn,date,label,slug,how in V if k in U[lob]]
    lines.append('Present in: '+', '.join(f'{names[l][:2]} ({d})' for l,d,_ in pres)+'\n\n')
    lines.append('Numbered as: '+', '.join(f'{names[l][:2]}: {U[l][k][0]}' for l,d,_ in pres)+'\n\n')
    absent=[names[lob][:2] for lob,*_ in V if k not in U[lob]]
    if absent: lines.append('Absent from: '+', '.join(absent)+'\n\n')
    prev=None
    for lob,date,label in pres:
        cur=U[lob][k][1]
        lines.append(f'\n## {names[lob]} ({label})\n')
        if prev is None:
            lines.append('First appearance under this key.\n\n```text\n'+'\n\n'.join(cur)+'\n```\n')
        elif prev==cur:
            lines.append('Unchanged from the previous version that has it.\n')
        else:
            fa=tempfile.NamedTemporaryFile('w',delete=False,encoding='utf-8'); fa.write('\n'.join(prev)+'\n'); fa.close()
            fb=tempfile.NamedTemporaryFile('w',delete=False,encoding='utf-8'); fb.write('\n'.join(cur)+'\n'); fb.close()
            w=gitdiff(fa.name,fb.name,True,9999)
            w='\n'.join(l for l in w.splitlines() if not l.startswith(('diff --git','index ','--- ','+++ ','@@')))
            lines.append('Changes (word diff, full text):\n\n```text\n'+w.replace('\n','\n\n')+'\n```\n')
        prev=cur
    open(p('sections',f'{k}.md'),'w',encoding='utf-8').write(''.join(lines))
print('versions:',len(V),'section keys:',keys)
