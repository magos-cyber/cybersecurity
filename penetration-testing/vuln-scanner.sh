#!/bin/bash
# Vulnerability Scanner
# Checks for common vulnerabilities and misconfigurations

set -euo pipefail

TARGET="${1:?Usage: $0 <target>}"

echo "=== Vulnerability Scanner ==="
echo "Target: $TARGET"
echo ""

# Check for open ports
echo "--- Open Ports ---"
for port in 21 22 23 25 53 80 110 143 443 445 993 3306 3389 5432 8080 8443; do
    timeout 1 bash -c "echo >/dev/tcp/$TARGET/$port" 2>/dev/null && echo "  [OPEN] $port"
done

# Check for anonymous FTP
echo ""
echo "--- FTP Checks ---"
if timeout 3 bash -c "echo >/dev/tcp/$TARGET/21" 2>/dev/null; then
    if echo -e "USER anonymous\r\nPASS anonymous\r\nQUIT" | timeout 3 nc -w 2 "$TARGET" 21 2>/dev/null | grep -q "230"; then
        echo "  [VULN] Anonymous FTP allowed"
    fi
fi

# Check for SMTP open relay
echo ""
echo "--- SMTP Checks ---"
if timeout 3 bash -c "echo >/dev/tcp/$TARGET/25" 2>/dev/null; then
    echo "  [INFO] SMTP port open - check for open relay manually"
fi

# Check SSL/TLS
echo ""
echo "--- SSL/TLS Checks ---"
if timeout 3 bash -c "echo >/dev/tcp/$TARGET/443" 2>/dev/null; then
    echo | timeout 3 openssl s_client -connect "$TARGET:443" 2>/dev/null | grep -E "Protocol|Cipher" || true
fi

echo ""
echo "Scan complete"
