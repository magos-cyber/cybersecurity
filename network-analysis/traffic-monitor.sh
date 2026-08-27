#!/bin/bash
# Network Traffic Monitor
# Monitors bandwidth and connections

set -euo pipefail

INTERFACE="${1:-eth0}"
INTERVAL="${2:-5}"

echo "=== Network Traffic Monitor ==="
echo "Interface: $INTERFACE"
echo "Interval: ${INTERVAL}s"
echo "Press Ctrl+C to stop"
echo ""

while true; do
    RX1=$(cat "/sys/class/net/$INTERFACE/statistics/rx_bytes" 2>/dev/null || echo 0)
    TX1=$(cat "/sys/class/net/$INTERFACE/statistics/tx_bytes" 2>/dev/null || echo 0)
    
    sleep "$INTERVAL"
    
    RX2=$(cat "/sys/class/net/$INTERFACE/statistics/rx_bytes" 2>/dev/null || echo 0)
    TX2=$(cat "/sys/class/net/$INTERFACE/statistics/tx_bytes" 2>/dev/null || echo 0)
    
    RX_RATE=$(( (RX2 - RX1) / INTERVAL ))
    TX_RATE=$(( (TX2 - TX1) / INTERVAL ))
    
    echo "$(date '+%H:%M:%S') RX: $(numfmt --to=iec $RX_RATE)/s | TX: $(numfmt --to=iec $TX_RATE)/s"
done
