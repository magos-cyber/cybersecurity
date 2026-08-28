#!/usr/bin/env python3
"""Checksum Verifier - Verifies file integrity using checksums."""

import hashlib
import sys
import os

def calculate_hash(filepath, algorithm='sha256'):
    """Calculate hash of a file."""
    hash_obj = hashlib.new(algorithm)
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def verify_file(filepath, expected_hash, algorithm='sha256'):
    """Verify a file against expected hash."""
    actual_hash = calculate_hash(filepath, algorithm)
    if actual_hash.lower() == expected_hash.lower():
        print(f"OK: {filepath} - hash matches")
        return True
    else:
        print(f"FAIL: {filepath} - hash mismatch")
        print(f"  Expected: {expected_hash}")
        print(f"  Actual:   {actual_hash}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: python checksum_verifier.py <file> <expected_hash> [algorithm]")
        sys.exit(1)
    
    filepath = sys.argv[1]
    expected = sys.argv[2]
    algorithm = sys.argv[3] if len(sys.argv) > 3 else 'sha256'
    
    verify_file(filepath, expected, algorithm)

if __name__ == "__main__":
    main()
