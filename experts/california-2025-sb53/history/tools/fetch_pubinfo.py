# Read members of the Legislature's bulk zip by HTTP range request (curl), without downloading 1.2 GB.
# python3 -I fetch_pubinfo.py list > listing.txt ; python3 -I fetch_pubinfo.py get OUTDIR MEMBER...
# SB 53 version blobs: BILL_VERSION_TBL_{114,2523,3705,5602,6563,7139,7772,8050,8894,8965}.lob (see BILL_VERSION_TBL.dat)

import sys, io, zipfile, subprocess, re
URL="https://downloads.leginfo.legislature.ca.gov/pubinfo_2025.zip"
class HF(io.RawIOBase):
    def __init__(s,url):
        s.url=url; s.pos=0
        h=subprocess.run(["curl","-sSI","-A","Mozilla/5.0",url],capture_output=True,text=True).stdout
        s.size=int(re.search(r"Content-Length: (\d+)",h,re.I).group(1))
    def seekable(s): return True
    def readable(s): return True
    def tell(s): return s.pos
    def seek(s,o,w=0):
        s.pos = o if w==0 else (s.pos+o if w==1 else s.size+o); return s.pos
    def read(s,n=-1):
        if n<0: n=s.size-s.pos
        if n==0 or s.pos>=s.size: return b""
        end=min(s.pos+n,s.size)-1
        d=subprocess.run(["curl","-sS","-A","Mozilla/5.0","-r",f"{s.pos}-{end}",s.url],capture_output=True,check=True).stdout
        s.pos+=len(d); return d
    def readinto(s,b):
        d=s.read(len(b)); b[:len(d)]=d; return len(d)
f=io.BufferedReader(HF(URL),buffer_size=1<<20)
z=zipfile.ZipFile(f)
cmd=sys.argv[1]
if cmd=="list":
    for i in z.infolist(): print(i.file_size, i.filename)
elif cmd=="get":
    out=sys.argv[2]
    for name in sys.argv[3:]:
        with z.open(name) as src, open(out+"/"+name.replace("/","_"),"wb") as dst:
            while True:
                c=src.read(1<<20)
                if not c: break
                dst.write(c)
        print("got",name)
