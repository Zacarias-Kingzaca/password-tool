from rich import print
import random
import string

"""
Password Strength Checker & Generator
Author: Zacarias Eduardo Joao
Description: Checks password strength and generates secure passwords
"""

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("- Use at least 8 characters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("- Add UPPERCASE letters")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("- Add lowercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("- Add NUMBERS")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("- Add SYMBOLS (!@#$%)")

    if score <= 2:
        strength = "[red] WEAK [/] ❌"
    elif score <= 4:
        strength = "[yellow] MEDIUM [/] ⚠️"
    else:
        strength = "[green] STRONG [/] ✅"

    return strength, feedback

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# --- Main Program ---
print("=== PASSWORD SECURITY TOOL ===")
user_pass = input("Enter a password to check: ")

strength, tips = check_strength(user_pass)
print(f"\nPassword strength: {strength}")

if tips:
    print("How to improve:")
    for tip in tips:
        print(tip)

print("\n--- Strong Password Generator ---")
print(f"[blue] Secure suggestion (12 chars):[/] {generate_strong_password(12)}")
print(f"[blue] Extra strong suggestion (16 chars):[/] {generate_strong_password(16)}")

