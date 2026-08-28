#!/usr/bin/env python3
"""IP Reputation Checker - Checks IPs against threat intelligence feeds."""

import requests
import sys

def check_abuseipdb(ip, api_key):
    """Check IP against AbuseIPDB."""
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Key": api_key,
        "Accept": "application/json"
    }
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }
    
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        data = response.json()
        if 'data' in data:
            score = data['data']['abuseScore']
            print(f"IP: {ip} - Abuse Score: {score}/100")
            if score > 50:
                print(f"  WARNING: {ip} has high abuse score")
            return score
    except requests.RequestException as e:
        print(f"Error checking {ip}: {e}")
        return None

def main():
    if len(sys.argv) < 3:
        print("Usage: python reputation_check.py <ip> <api_key>")
        sys.exit(1)
    
    check_abuseipdb(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
