#!/bin/bash
# Packet Capture Helper
# Simplified tcpdump wrapper for common capture scenarios

set -euo pipefail

INTERFACE="${1:-eth0}"
DURATION="${2:-60}"
OUTPUT="${3:-/tmp/capture.pcap}"

echo "=== Packet Capture ==="
echo "Interface: $INTERFACE"
echo "Duration: ${DURATION}s"
echo "Output: $OUTPUT"
echo ""

# Check if running as root
if [ "$(id -u)" -ne 0 ]; then
    echo "Error: Must run as root"
    exit 1
fi

# Capture
echo "Starting capture..."
timeout "$DURATION" tcpdump -i "$INTERFACE" -w "$OUTPUT" 2>/dev/null || true

echo ""
echo "Capture complete"
echo "Analyze with: tcpdump -r $OUTPUT"
echo "Or with Wireshark: wireshark $OUTPUT"
