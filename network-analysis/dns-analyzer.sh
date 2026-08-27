#!/bin/bash
# DNS Analyzer
# Analyzes DNS queries and responses

set -euo pipefail

DOMAIN="${1:?Usage: $0 <domain>}"

echo "=== DNS Analysis: $DOMAIN ==="

# A record
echo "--- A Record ---"
dig +short A "$DOMAIN"

# AAAA record
echo ""
echo "--- AAAA Record ---"
dig +short AAAA "$DOMAIN"

# MX record
echo ""
echo "--- MX Record ---"
dig +short MX "$DOMAIN"

# NS record
echo ""
echo "--- NS Record ---"
dig +short NS "$DOMAIN"

# TXT record
echo ""
echo "--- TXT Record ---"
dig +short TXT "$DOMAIN"

# WHOIS
echo ""
echo "--- WHOIS ---"
whois "$DOMAIN" 2>/dev/null | head -10

echo ""
echo "Analysis complete"
