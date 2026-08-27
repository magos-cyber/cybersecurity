#!/bin/bash
# Advanced Port Scanner
# Performs TCP/UDP port scanning with service detection

set -euo pipefail

HOST="${1:?Usage: $0 <host> [start-port] [end-port]}"
START_PORT="${2:-1}"
END_PORT="${3:-1024}"
TIMEOUT="${4:-1}"

echo "=== Port Scanner ==="
echo "Target: $HOST"
echo "Ports: $START_PORT-$END_PORT"
echo "Timeout: ${TIMEOUT}s"
echo ""

# Common service ports
COMMON_PORTS="21 22 23 25 53 80 110 111 135 139 143 443 445 993 995 1723 3306 3389 5900 8080 8443"

# Scan common ports first
echo "Scanning common ports..."
for port in $COMMON_PORTS; do
    timeout "$TIMEOUT" bash -c "echo >/dev/tcp/$HOST/$port" 2>/dev/null &&         echo "[OPEN] Port $port ($(grep -w "^$port/" /etc/services 2>/dev/null | head -1 | awk '{print $1}' || echo 'unknown'))" &
done
wait

# Scan range
echo ""
echo "Scanning port range $START_PORT-$END_PORT..."
for ((port=START_PORT; port<=END_PORT; port++)); do
    timeout "$TIMEOUT" bash -c "echo >/dev/tcp/$HOST/$port" 2>/dev/null &&         echo "[OPEN] Port $port" &
    if ((port % 50 == 0)); then wait; fi
done
wait

echo ""
echo "Scan complete"
