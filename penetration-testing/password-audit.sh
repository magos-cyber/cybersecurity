#!/bin/bash
# Password Security Audit
# Checks for weak passwords and password policies

set -euo pipefail

echo "=== Password Security Audit ==="

# Check password policy
echo "--- Password Policy ---"
grep -E "^PASS_" /etc/login.defs 2>/dev/null

# Check for empty passwords
echo ""
echo "--- Empty Passwords ---"
awk -F: '($2 == "") {print $1}' /etc/shadow 2>/dev/null || echo "  Cannot read shadow file"

# Check for passwordless accounts
echo ""
echo "--- Passwordless Accounts ---"
awk -F: '($2 == "*") {print $1}' /etc/shadow 2>/dev/null || echo "  Cannot read shadow file"

# Check SSH key auth
echo ""
echo "--- SSH Key Authentication ---"
grep -E "^(PasswordAuthentication|PubkeyAuthentication)" /etc/ssh/sshd_config 2>/dev/null

echo ""
echo "Audit complete"
