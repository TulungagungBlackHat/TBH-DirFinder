#!/usr/bin/env python3
# TBH-DirFinder v2.0 Pro - + 403 Bypass
import requests, argparse, json
from concurrent.futures import ThreadPoolExecutor

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-DirFinder v2.0 Pro \033[91m- 403 Bypass \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

COMMON = ["admin","login","api",".git",".env","backup","config","dashboard","test","dev","staging","backup.zip",".htaccess","robots.txt","sitemap.xml","swagger"]

def check(url, path):
    full=f"{url.rstrip('/')}/{path.lstrip('/')}"
    headers_list=[{}, {"X-Original-URL":f"/{path}"}, {"X-Custom-IP-Authorization":"127.0.0.1"}]
    for h in headers_list:
        try:
            r=requests.get(full,timeout=3,headers={'User-Agent':'TBH-DirFinder/2.0',**h},allow_redirects=False)
            if r.status_code in [200,301,302,403,401]:
                bypass = " [BYPASS?]" if h and r.status_code==200 else ""
                return {"path":path,"url":full,"status":r.status_code,"size":len(r.content),"bypass":bool(bypass),"header":str(h) if h else "normal"}
        except: pass
    return None

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan!\033[0m\n")
    parser=argparse.ArgumentParser(description="v2.0 Pro")
    parser.add_argument("-u","--url",required=True)
    parser.add_argument("-w","--wordlist",help="Custom wordlist")
    parser.add_argument("-t","--threads",type=int,default=20)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    paths=COMMON
    if args.wordlist:
        with open(args.wordlist) as f: paths=[l.strip() for l in f if l.strip()]
    print(f"[*] {args.url} | {len(paths)} paths | 20 threads | +403 bypass")
    found=[]
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        results=list(ex.map(lambda p: check(args.url,p), paths))
    for r in results:
        if r:
            found.append(r)
            flag=" \033[92m[BYPASS?]\033[0m" if r["bypass"] else ""
            print(f"\033[92m[FOUND] {r['status']} {r['url']} ({r['size']}){flag}\033[0m")
            if r["path"] in [".git",".env"]: print("  -> High!")
    print(f"\n[✓] Found {len(found)}")
    if args.json:
        open(args.json,'w').write(json.dumps({"target":args.url,"found":found},indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
