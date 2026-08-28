#!/usr/bin/env python3
"""Async Port Scanner."""

import asyncio
import argparse
from datetime import datetime

async def scan_port(host, port, timeout=1):
    """Scan a single port asynchronously."""
    try:
        _, writer = await asyncio.wait_for(
            asyncio.open_connection(host, port),
            timeout=timeout
        )
        writer.close()
        return port, True
    except (asyncio.TimeoutError, ConnectionRefusedError, OSError):
        return port, False

async def scan_range(host, start, end):
    """Scan a range of ports."""
    tasks = [scan_port(host, port) for port in range(start, end + 1)]
    results = await asyncio.gather(*tasks)
    open_ports = [port for port, is_open in results if is_open]
    return open_ports

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host")
    parser.add_argument("-s", "--start", type=int, default=1)
    parser.add_argument("-e", "--end", type=int, default=1024)
    args = parser.parse_args()
    
    print(f"Scanning {args.host} ports {args.start}-{args.end}...")
    start_time = datetime.now()
    
    open_ports = asyncio.run(scan_range(args.host, args.start, args.end))
    
    elapsed = datetime.now() - start_time
    print(f"
Open ports ({len(open_ports)}): {open_ports}")
    print(f"Scan completed in {elapsed.total_seconds():.2f}s")

if __name__ == "__main__":
    main()
