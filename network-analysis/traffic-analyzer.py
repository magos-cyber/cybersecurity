#!/usr/bin/env python3
"""Network Traffic Analyzer - Analyzes pcap files for anomalies."""

import sys
from collections import Counter

def analyze_pcap(pcap_file):
    """Analyze a pcap file (requires scapy)."""
    try:
        from scapy.all import rdpcap, IP, TCP, UDP
    except ImportError:
        print("scapy not installed. Install with: pip install scapy")
        sys.exit(1)
    
    packets = rdpcap(pcap_file)
    
    protocols = Counter()
    src_ips = Counter()
    dst_ips = Counter()
    
    for pkt in packets:
        if IP in pkt:
            src_ips[pkt[IP].src] += 1
            dst_ips[pkt[IP].dst] += 1
            if TCP in pkt:
                protocols['TCP'] += 1
            elif UDP in pkt:
                protocols['UDP'] += 1
            else:
                protocols['Other'] += 1
    
    print(f"=== Analysis of {pcap_file} ===")
    print(f"Total packets: {len(packets)}
")
    
    print("Protocols:")
    for proto, count in protocols.most_common():
        print(f"  {proto}: {count}")
    
    print("
Top source IPs:")
    for ip, count in src_ips.most_common(10):
        print(f"  {ip}: {count}")
    
    print("
Top destination IPs:")
    for ip, count in dst_ips.most_common(10):
        print(f"  {ip}: {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python traffic_analyzer.py <pcap-file>")
        sys.exit(1)
    
    analyze_pcap(sys.argv[1])

if __name__ == "__main__":
    main()
