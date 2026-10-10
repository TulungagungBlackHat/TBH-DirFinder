# TBH-DirFinder

<p align="center">
  <a href="https://github.com/TulungagungBlackHat/TBH-DirFinder/actions/workflows/ci.yml"><img src="https://github.com/TulungagungBlackHat/TBH-DirFinder/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="License">
  <img src="https://img.shields.io/badge/python-3.8%2B-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/detects-.git%20.env-red.svg" alt="Detects .git/.env">
</p>

Content discovery with a bias toward **the exposures that actually pay**: `.git` directories, `.env` files, backup archives, and admin panels.

Part of the [Tulungagung Black Hat](https://github.com/TulungagungBlackHat) toolset.

## What It Checks

- Sensitive files: `.env`, `.git/config`, `.git/HEAD`, `.DS_Store`
- Backup patterns: `.bak`, `.old`, `.zip`, `.sql`
- Common admin/login panels and config paths
- Status-code aware (200 / 403 / 301 reported distinctly)
- Custom wordlist and thread control

## Install

```bash
git clone https://github.com/TulungagungBlackHat/TBH-DirFinder
cd TBH-DirFinder
pip install -r requirements.txt
```

## Usage

```
usage: dirfinder.py [-h] -u URL [-w WORDLIST] [-t THREADS] [--json JSON]

options:
  -u, --url URL          Target base URL
  -w, --wordlist WORDLIST    Custom wordlist (one path per line)
  -t, --threads THREADS      Concurrent requests
  --json JSON                Save JSON
```

### Examples

```bash
python3 dirfinder.py -u https://example.com
python3 dirfinder.py -u https://example.com -w raft-small-words.txt -t 20 --json found.json
```

## Sample Output

```
[*] https://example.com | 40 paths | 10 threads
[FOUND] 200 https://example.com/.git/config
[FOUND] 403 https://example.com/admin
[NOT]   404 https://example.com/backup.zip

[✓] Found 2 | JSON: found.json
```

A hit on `.git` or `.env` is usually High/Critical (source code or secrets exposure) — grab proof carefully and report through the program, not through a public gist.

## Authorized Use Only

Brute-forcing paths is active scanning — only within authorized scopes. See [SECURITY.md](SECURITY.md).

## Related Tools

- [TBH-JSLeak](https://github.com/TulungagungBlackHat/TBH-JSLeak) — secrets inside JS files you found
- [TBH-SubFinder](https://github.com/TulungagungBlackHat/TBH-SubFinder) — find the hosts to scan first

## License

[MIT](LICENSE) — Tulungagung Black Hat, East Java, Indonesia. Always Smile :)
