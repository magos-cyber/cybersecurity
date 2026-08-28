#!/usr/bin/env python3
"""Simple Hash Cracker - Dictionary attack against common hashes."""

import hashlib
import argparse
import sys

SUPPORTED = {
    'md5': hashlib.md5,
    'sha1': hashlib.sha1,
    'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,
}

def crack(target_hash, algorithm, wordlist):
    """Attempt to crack a hash."""
    hasher = SUPPORTED.get(algorithm.lower())
    if not hasher:
        print(f"Unsupported algorithm: {algorithm}")
        return None
    
    with open(wordlist) as f:
        for line in f:
            word = line.strip()
            if hasher(word.encode()).hexdigest() == target_hash:
                return word
    
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hash")
    parser.add_argument("-a", "--algorithm", default="sha256")
    parser.add_argument("-w", "--wordlist", required=True)
    args = parser.parse_args()
    
    print(f"Cracking {args.algorithm} hash: {args.hash}")
    result = crack(args.hash, args.algorithm, args.wordlist)
    
    if result:
        print(f"[FOUND] {args.hash} = {result}")
    else:
        print("[NOT FOUND] Password not in wordlist")

if __name__ == "__main__":
    main()
