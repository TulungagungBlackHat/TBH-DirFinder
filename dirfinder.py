#!/usr/bin/env python3
# TBH-DirFinder - Bug Bounty Directory Finder (Educational)
import requests, argparse, json
from concurrent.futures import ThreadPoolExecutor

BANNER = """\033[91m╔════════════════════════════════════╗
\033[91m║ \033[97mTBH-DirFinder \033[91m- Bug Bounty          \033[91m║
\033[91m║ \033[90mTulungagung Black Hat | uchil404 \033[91m║
\033[91m╚════════════════════════════════════╝\033[0m"""

COMMON = ["admin","login","api",".git",".env","backup","config","dashboard","test","dev","staging","backup.zip",".htaccess","robots.txt","sitemap.xml","swagger","api/docs"]

def check(url, path):
    full=f"{url.rstrip('/')}/{path.lstrip('/')}"
    try:
        r=requests.get(full,timeout=3,headers={'User-Agent':'TBH-DirFinder/1.0'},allow_redirects=False)
        if r.status_code in [200,301,302,403]:
            return {"path":path,"url":full,"status":r.status_code,"size":len(r.content)}
    except: pass
    return None

def main():
    print(BANNER)
    print("\033[91m[!] Hanya untuk scope yang diizinkan!\033[0m\n")
    parser=argparse.ArgumentParser(description="DirFinder")
    parser.add_argument("-u","--url",required=True,help="Target URL")
    parser.add_argument("-w","--wordlist",help="Custom wordlist")
    parser.add_argument("-t","--threads",type=int,default=20)
    parser.add_argument("--json",help="Save JSON")
    args=parser.parse_args()
    paths=COMMON
    if args.wordlist:
        with open(args.wordlist) as f: paths=[l.strip() for l in f if l.strip()]
    print(f"[*] {args.url} | {len(paths)} paths | {args.threads} threads")
    found=[]
    with ThreadPoolExecutor(max_workers=args.threads) as ex:
        results=list(ex.map(lambda p: check(args.url,p), paths))
    for r in results:
        if r:
            found.append(r)
            color="\033[92m" if r["status"]==200 else "\033[93m"
            print(f"{color}[FOUND] {r['status']} {r['url']} ({r['size']} bytes)\033[0m")
            if r["path"] in [".git",".env","backup.zip"]: print("  -> Potensi High! File sensitif")
    print(f"\n[✓] Found {len(found)}")
    if args.json:
        open(args.json,'w').write(json.dumps({"target":args.url,"found":found},indent=2)); print(f"[✓] JSON: {args.json}")

if __name__=="__main__": main()
