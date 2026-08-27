#!/bin/bash
# Digital Forensics Collector
# Collects system artifacts for incident response

set -euo pipefail

OUTPUT_DIR="${1:-/tmp/forensics-$(date +%Y%m%d-%H%M%S)}"

echo "=== Forensics Collector ==="
echo "Output: $OUTPUT_DIR"

mkdir -p "$OUTPUT_DIR"/{logs,network,processes,users,files}

# System info
echo "Collecting system info..."
uname -a > "$OUTPUT_DIR/system.txt"
date >> "$OUTPUT_DIR/system.txt"
uptime >> "$OUTPUT_DIR/system.txt"

# Logs
echo "Collecting logs..."
cp /var/log/auth.log "$OUTPUT_DIR/logs/" 2>/dev/null || true
cp /var/log/syslog "$OUTPUT_DIR/logs/" 2>/dev/null || true
cp /var/log/kern.log "$OUTPUT_DIR/logs/" 2>/dev/null || true

# Network connections
echo "Collecting network info..."
ss -tulpn > "$OUTPUT_DIR/network/connections.txt" 2>/dev/null || true
iptables -L -n > "$OUTPUT_DIR/network/firewall.txt" 2>/dev/null || true
cat /etc/hosts > "$OUTPUT_DIR/network/hosts.txt"

# Processes
echo "Collecting process info..."
ps auxf > "$OUTPUT_DIR/processes/ps.txt"
lsof > "$OUTPUT_DIR/processes/lsof.txt" 2>/dev/null || true

# Users
echo "Collecting user info..."
who > "$OUTPUT_DIR/users/logged_in.txt"
last -50 > "$OUTPUT_DIR/users/last_logins.txt" 2>/dev/null || true
cat /etc/passwd > "$OUTPUT_DIR/users/passwd.txt"

# Suspicious files
echo "Checking for suspicious files..."
find /tmp -type f -mtime -1 > "$OUTPUT_DIR/files/recent_tmp.txt" 2>/dev/null || true
find / -perm -4000 -type f > "$OUTPUT_DIR/files/suid_files.txt" 2>/dev/null || true

# Create archive
echo ""
echo "Creating archive..."
tar -czf "$OUTPUT_DIR.tar.gz" "$OUTPUT_DIR"
echo "Forensics data: $OUTPUT_DIR.tar.gz"
