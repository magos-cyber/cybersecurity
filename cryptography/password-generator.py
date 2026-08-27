#!/usr/bin/env python3
"""Secure Password Generator."""
import secrets
import string
import sys

def generate_password(length=20, use_special=True):
    """Generate a secure random password."""
    alphabet = string.ascii_letters + string.digits
    if use_special:
        alphabet += string.punctuation
    
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    return password

def generate_passphrase(words=5):
    """Generate a memorable passphrase."""
    # Simple word list (in production, use a larger dictionary)
    wordlist = ["correct", "horse", "battery", "staple", "purple", "monkey", 
                "dishwasher", "galaxy", "python", "thunder", "ocean", "mountain"]
    
    passphrase = " ".join(secrets.choice(wordlist) for _ in range(words))
    return passphrase

if __name__ == "__main__":
    length = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(f"Password: {generate_password(length)}")
    print(f"Passphrase: {generate_passphrase()}")
