#!/bin/bash
# Web Reconnaissance
# Gathers information about web targets

set -euo pipefail

URL="${1:?Usage: $0 <url>}"

echo "=== Web Reconnaissance ==="
echo "Target: $URL"
echo ""

# HTTP headers
echo "--- HTTP Headers ---"
curl -sI -L --max-time 10 "$URL" 2>/dev/null | head -20

# Technologies
echo ""
echo "--- Technologies ---"
curl -sL --max-time 10 "$URL" 2>/dev/null | grep -oE '<meta[^>]+>' | head -10

# Robots.txt
echo ""
echo "--- robots.txt ---"
curl -sL --max-time 10 "$URL/robots.txt" 2>/dev/null | head -20

# Sitemap
echo ""
echo "--- Sitemap ---"
curl -sL --max-time 10 "$URL/sitemap.xml" 2>/dev/null | head -10

echo ""
echo "Recon complete"
