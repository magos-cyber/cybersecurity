#!/usr/bin/env python3
"""Directory Buster - Discovers hidden directories and files."""

import requests
import sys
import argparse

def dir_bust(url, wordlist, extensions=None, threads=10):
    """Brute force directories."""
    found = []
    
    with open(wordlist) as f:
        words = [line.strip() for line in f if line.strip()]
    
    base_url = url.rstrip('/')
    extensions = extensions or ['']
    
    for word in words:
        for ext in extensions:
            path = f"{base_url}/{word}{ext}"
            try:
                resp = requests.get(path, timeout=3, allow_redirects=False)
                if resp.status_code in (200, 204, 301, 302, 307, 401, 403):
                    print(f"[{resp.status_code}] {path}")
                    found.append(path)
            except requests.RequestException:
                pass
    
    return found

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Target URL")
    parser.add_argument("-w", "--wordlist", required=True)
    parser.add_argument("-e", "--extensions", default="")
    parser.add_argument("-t", "--threads", type=int, default=10)
    args = parser.parse_args()
    
    exts = [e.strip() for e in args.extensions.split(',') if e.strip()]
    exts = [f".{e}" if not e.startswith('.') else e for e in exts] or ['']
    
    print(f"Starting directory busting on {args.url}")
    results = dir_bust(args.url, args.wordlist, exts, args.threads)
    print(f"
Found {len(results)} paths")
