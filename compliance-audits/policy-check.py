#!/usr/bin/env python3
"""Security Policy Compliance Checker."""
import os
import subprocess

POLICIES = {
    "password_min_length": {"file": "/etc/login.defs", "grep": "PASS_MIN_LEN", "expected": "12"},
    "password_max_days": {"file": "/etc/login.defs", "grep": "PASS_MAX_DAYS", "expected": "90"},
    "password_min_days": {"file": "/etc/login.defs", "grep": "PASS_MIN_DAYS", "expected": "7"},
}

def check_policy(name, config):
    """Check a single policy."""
    filepath = config["file"]
    grep_pattern = config["grep"]
    expected = config["expected"]
    
    if not os.path.exists(filepath):
        return "SKIP", f"File not found: {filepath}"
    
    result = subprocess.run(
        ["grep", f"^{grep_pattern}", filepath],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        return "FAIL", f"Setting not found"
    
    actual = result.stdout.strip().split()[1] if len(result.stdout.strip().split()) > 1 else ""
    
    if actual == expected:
        return "PASS", f"{actual}"
    else:
        return "FAIL", f"Expected {expected}, got {actual}"

def main():
    print("=== Security Policy Compliance ===")
    
    passed = failed = skipped = 0
    
    for name, config in POLICIES.items():
        status, detail = check_policy(name, config)
        print(f"[{status}] {name}: {detail}")
        
        if status == "PASS":
            passed += 1
        elif status == "FAIL":
            failed += 1
        else:
            skipped += 1
    
    print(f"\nSummary: {passed} passed, {failed} failed, {skipped} skipped")

if __name__ == "__main__":
    main()
