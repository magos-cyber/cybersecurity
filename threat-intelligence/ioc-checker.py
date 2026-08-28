#!/usr/bin/env python3
"""IOC Checker - Checks IPs/domains against threat intelligence feeds."""

import requests
import argparse
import hashlib
import json

# AbuseIPDB (replace with your API key via env)
ABUSEIPDB_KEY = "YOUR_API_KEY_HERE"

def check_ip_abuseipdb(ip):
    """Check IP against AbuseIPDB."""
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': ABUSEIPDB_KEY,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    try:
        resp = requests.get(url, headers=headers, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            score = data['data']['abuseScore']
            print(f"IP {ip}: AbuseIPDB score = {score}")
            return score
    except Exception as e:
        print(f"Error checking {ip}: {e}")
    return None

def check_hash_virustotal(file_hash, api_key):
    """Check file hash against VirusTotal."""
    url = f"https://www.virustotal.com/vtapi/v2/file/report"
    params = {
        'apikey': api_key,
        'resource': file_hash
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            positives = data.get('positives', 0)
            print(f"Hash {file_hash}: {positives} detections")
            return positives
    except Exception as e:
        print(f"Error checking hash: {e}")
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip")
    parser.add_argument("-f", "--file", help="File to hash and check")
    parser.add_argument("-k", "--apikey")
    args = parser.parse_args()
    
    if args.ip:
        check_ip_abuseipdb(args.ip)
    
    if args.file:
        with open(args.file, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        if args.apikey:
            check_hash_virustotal(file_hash, args.apikey)
        else:
            print(f"SHA256: {file_hash}")

if __name__ == "__main__":
    main()
