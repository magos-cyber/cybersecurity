#!/bin/bash
# CIS Benchmark Audit
# Checks system against CIS benchmark recommendations

set -euo pipefail

echo "=== CIS Benchmark Audit ==="
echo "Date: $(date)"
echo ""

PASS=0
FAIL=0
WARN=0

check() {
    local description="$1"
    local command="$2"
    local expected="$3"
    
    actual=$(eval "$command" 2>/dev/null || echo "N/A")
    
    if [ "$actual" = "$expected" ]; then
        echo "[PASS] $description"
        ((PASS++))
    elif [ "$actual" = "N/A" ]; then
        echo "[WARN] $description (cannot check)"
        ((WARN++))
    else
        echo "[FAIL] $description (expected: $expected, got: $actual)"
        ((FAIL++))
    fi
}

# SSH Configuration
echo "--- SSH Configuration ---"
check "SSH Protocol 2" "grep '^Protocol' /etc/ssh/sshd_config 2>/dev/null | awk '{print $2}'" "2"
check "Root login disabled" "grep '^PermitRootLogin' /etc/ssh/sshd_config 2>/dev/null | awk '{print $2}'" "no"
check "Password auth disabled" "grep '^PasswordAuthentication' /etc/ssh/sshd_config 2>/dev/null | awk '{print $2}'" "no"

# Kernel Parameters
echo ""
echo "--- Kernel Parameters ---"
check "ASLR enabled" "sysctl -n kernel.randomize_va_space" "2"
check "IP forwarding disabled" "sysctl -n net.ipv4.ip_forward" "0"
check "ICMP broadcasts ignored" "sysctl -n net.ipv4.icmp_echo_ignore_broadcasts" "1"

# File Permissions
echo ""
echo "--- File Permissions ---"
check "/etc/passwd permissions" "stat -c %a /etc/passwd" "644"
check "/etc/shadow permissions" "stat -c %a /etc/shadow" "640"

# Services
echo ""
echo "--- Services ---"
check "UFW enabled" "ufw status 2>/dev/null | head -1 | awk '{print $2}'" "active"

echo ""
echo "=== Summary ==="
echo "PASS: $PASS"
echo "FAIL: $FAIL"
echo "WARN: $WARN"
