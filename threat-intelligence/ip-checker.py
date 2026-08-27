#!/usr/bin/env python3
# IP Reputation Checker
# Checks IP against threat intelligence feeds

import json
import urllib.request

def check_ip_abuseipdb(ip, api_key):
    """Check IP reputation via AbuseIPDB."""
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}"
    req = urllib.request.Request(url, headers={
        "Key": api_key,
        "Accept": "application/json"
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", {})
    except Exception as e:
        return {"error": str(e)}

def check_ip_virustotal(ip, api_key):
    """Check IP reputation via VirusTotal."""
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    req = urllib.request.Request(url, headers={
        "x-apikey": api_key
    })
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return data.get("data", {})
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys
    ip = sys.argv[1] if len(sys.argv) > 1 else "8.8.8.8"
    print(f"Checking IP: {ip}")
    print("Note: Requires API keys for AbuseIPDB and VirusTotal")
