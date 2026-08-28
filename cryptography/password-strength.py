#!/usr/bin/env python3
"""Password Strength Checker."""

import re
import argparse

def check_strength(password):
    """Evaluate password strength."""
    score = 0
    feedback = []
    
    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Too short (min 8 chars)")
    
    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    # Digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    # Special chars
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Common patterns
    if re.search(r'(.)', password):
        score -= 1
        feedback.append("Avoid repeated characters")
    
    # Entropy estimate
    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password): charset += 32
    import math
    entropy = len(password) * math.log2(charset) if charset else 0
    
    return score, feedback, entropy

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("password")
    args = parser.parse_args()
    
    score, feedback, entropy = check_strength(args.password)
    
    print(f"Password Entropy: {entropy:.1f} bits")
    print(f"Score: {score}/7")
    
    if score >= 6 and entropy > 60:
        print("Strength: STRONG")
    elif score >= 4:
        print("Strength: MEDIUM")
    else:
        print("Strength: WEAK")
    
    if feedback:
        print("
Suggestions:")
        for f in feedback:
            print(f"  - {f}")

if __name__ == "__main__":
    main()
