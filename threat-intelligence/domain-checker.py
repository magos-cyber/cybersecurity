#!/usr/bin/env python3
# Domain Reputation Checker
# Checks domain against threat intelligence

import json
import urllib.request
import socket

def resolve_domain(domain):
    """Resolve domain to IP addresses."""
    try:
        ips = socket.getaddrinfo(domain, None)
        return list(set(ip[4][0] for ip in ips))
    except socket.gaierror:
        return []

def check_url_virustotal(url, api_key):
    """Check URL reputation via VirusTotal."""
    encoded_url = urllib.parse.quote(url, safe="")
    api_url = f"https://www.virustotal.com/api/v3/urls/{encoded_url}"
    req = urllib.request.Request(api_url, headers={"x-apikey": api_key})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    domain = sys.argv[1] if len(sys.argv) > 1 else "example.com"
    print(f"Checking domain: {domain}")
    ips = resolve_domain(domain)
    print(f"Resolved IPs: {ips}")
