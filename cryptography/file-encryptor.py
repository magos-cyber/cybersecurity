#!/usr/bin/env python3
"""File Encryption/Decryption Tool."""
import os
import sys
from cryptography.fernet import Fernet

def generate_key():
    """Generate encryption key."""
    return Fernet.generate_key()

def encrypt_file(filepath, key):
    """Encrypt a file."""
    f = Fernet(key)
    with open(filepath, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filepath + ".enc", "wb") as file:
        file.write(encrypted)
    print(f"Encrypted: {filepath}.enc")

def decrypt_file(filepath, key):
    """Decrypt a file."""
    f = Fernet(key)
    with open(filepath, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    output = filepath.replace(".enc", ".dec")
    with open(output, "wb") as file:
        file.write(decrypted)
    print(f"Decrypted: {output}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python file-encryptor.py <encrypt|decrypt> <file> [key_file]")
        sys.exit(1)
    
    action = sys.argv[1]
    filepath = sys.argv[2]
    key_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    if key_file:
        with open(key_file, "rb") as f:
            key = f.read()
    else:
        key = generate_key()
        with open(filepath + ".key", "wb") as f:
            f.write(key)
        print(f"Key saved to: {filepath}.key")
    
    if action == "encrypt":
        encrypt_file(filepath, key)
    elif action == "decrypt":
        decrypt_file(filepath, key)
