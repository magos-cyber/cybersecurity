#!/usr/bin/env python3
"""Disk Forensics Collector - Collects forensic artifacts from a system."""

import os
import subprocess
import hashlib
import sys
from datetime import datetime

def collect_system_info():
    """Collect basic system information."""
    info = {}
    info['timestamp'] = datetime.now().isoformat()
    info['hostname'] = os.uname().nodename if hasattr(os, 'uname') else 'unknown'
    
    # Collect running processes
    result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    info['processes'] = result.stdout
    
    # Collect network connections
    result = subprocess.run(['ss', '-tulnp'], capture_output=True, text=True)
    info['network'] = result.stdout
    
    # Collect mounted filesystems
    result = subprocess.run(['mount'], capture_output=True, text=True)
    info['mounts'] = result.stdout
    
    return info

def calculate_hash(filepath):
    """Calculate SHA256 hash of a file."""
    hash_obj = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def main():
    output_dir = sys.argv[1] if len(sys.argv) > 1 else '/tmp/forensics'
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Collecting forensic data to {output_dir}...")
    
    info = collect_system_info()
    
    # Write system info
    with open(f"{output_dir}/system_info.txt", 'w') as f:
        f.write(f"Timestamp: {info['timestamp']}
")
        f.write(f"Hostname: {info['hostname']}

")
        f.write("=== Running Processes ===
")
        f.write(info['processes'])
        f.write("
=== Network Connections ===
")
        f.write(info['network'])
        f.write("
=== Mounted Filesystems ===
")
        f.write(info['mounts'])
    
    # Collect common log files
    log_files = ['/var/log/auth.log', '/var/log/syslog', '/var/log/messages']
    for log_file in log_files:
        if os.path.exists(log_file):
            dest = f"{output_dir}/{os.path.basename(log_file)}"
            subprocess.run(['cp', log_file, dest])
            hash_value = calculate_hash(dest)
            print(f"Collected {log_file} (hash: {hash_value[:16]}...)")
    
    print(f"Forensic collection complete. Data in {output_dir}")

if __name__ == "__main__":
    main()
