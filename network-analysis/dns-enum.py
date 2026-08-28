#!/usr/bin/env python3
"""DNS Enumeration Tool."""

import socket
import argparse
import dns.resolver
import dns.zone
import dns.query

def get_records(domain, record_type):
    """Get DNS records of a type."""
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(r) for r in answers]
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.NoNameservers):
        return []

def enumerate_common(domain):
    """Enumerate common DNS record types."""
    types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA', 'CNAME']
    results = {}
    
    for t in types:
        records = get_records(domain, t)
        if records:
            results[t] = records
            print(f"{t}: {', '.join(records)}")
    
    return results

def reverse_dns(ip):
    """Reverse DNS lookup."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except (socket.herror, socket.gaierror):
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("domain")
    parser.add_argument("-r", "--reverse", help="Reverse lookup an IP")
    args = parser.parse_args()
    
    if args.reverse:
        host = reverse_dns(args.reverse)
        print(f"{args.reverse} -> {host}")
    else:
        enumerate_common(args.domain)
