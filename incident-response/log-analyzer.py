#!/usr/bin/env python3
"""Security Log Analyzer."""
import re
from collections import Counter
from datetime import datetime

def analyze_auth_log(logfile="/var/log/auth.log"):
    """Analyze authentication log."""
    failed_attempts = Counter()
    successful_logins = Counter()
    blocked_ips = Counter()
    
    try:
        with open(logfile) as f:
            for line in f:
                # Failed password
                if "Failed password" in line:
                    match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        failed_attempts[match.group(1)] += 1
                
                # Successful login
                if "Accepted" in line and "from" in line:
                    match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        successful_logins[match.group(1)] += 1
                
                # Blocked IP
                if "Blocked" in line or "DENIED" in line:
                    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
                    if match:
                        blocked_ips[match.group(1)] += 1
    except FileNotFoundError:
        print(f"Log file not found: {logfile}")
        return
    
    print("=== Failed SSH Attempts ===")
    for ip, count in failed_attempts.most_common(10):
        print(f"  {ip}: {count} attempts")
    
    print("\n=== Successful Logins ===")
    for ip, count in successful_logins.most_common(10):
        print(f"  {ip}: {count} logins")

if __name__ == "__main__":
    import sys
    logfile = sys.argv[1] if len(sys.argv) > 1 else "/var/log/auth.log"
    analyze_auth_log(logfile)
