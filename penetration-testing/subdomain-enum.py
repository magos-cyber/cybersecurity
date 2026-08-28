#!/usr/bin/env python3
"""Subdomain Enumerator - Finds subdomains for a target."""

import socket
import requests
import argparse

def resolve_subdomain(subdomain, domain):
    """Try to resolve a subdomain."""
    target = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(target)
        return target, ip
    except socket.gaierror:
        return None

def enumerate_from_wordlist(domain, wordlist):
    """Enumerate subdomains from wordlist."""
    results = []
    with open(wordlist) as f:
        subs = [line.strip() for line in f if line.strip()]
    
    for sub in subs:
        result = resolve_subdomain(sub, domain)
        if result:
            print(f"FOUND: {result[0]} -> {result[1]}")
            results.append(result)
    
    return results

def crtsh_enum(domain):
    """Query crt.sh for subdomains."""
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            subs = set()
            for entry in data:
                name = entry.get('name_value', '')
                for sub in name.split('
'):
                    if domain in sub:
                        subs.add(sub.strip())
            for sub in sorted(subs):
                print(f"CRT.SH: {sub}")
            return subs
    except Exception as e:
        print(f"Error querying crt.sh: {e}")
    return set()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    parser.add_argument("-w", "--wordlist")
    parser.add_argument("-c", "--crtsh", action="store_true")
    args = parser.parse_args()
    
    if args.wordlist:
        enumerate_from_wordlist(args.domain, args.wordlist)
    if args.crtsh:
        crtsh_enum(args.domain)
