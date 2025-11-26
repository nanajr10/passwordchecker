import re

# Optional: list of common passwords
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123", "111111", "password1"]

def check_password_strength(password):
    # Length check
    length = len(password) >= 8

    # Uppercase check
    upper = bool(re.search(r'[A-Z]', password))

    # Lowercase check
    lower = bool(re.search(r'[a-z]', password))

    # Number check
    number = bool(re.search(r'\d', password))

    # Special character check
    special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Common password check
    common = password.lower() in common_passwords

    # Score calculation
    score = sum([length, upper, lower, number, special])

    # Strength evaluation
    if common:
        strength = "Very Weak (Common Password)"
    elif score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, length, upper, lower, number, special, common

def main():
    password = input("Enter a password to check its strength: ")
    strength, length, upper, lower, number, special, common = check_password_strength(password)

    print("\nPassword Analysis:")
    print(f"Length >= 8: {length}")
    print(f"Contains Uppercase: {upper}")
    print(f"Contains Lowercase: {lower}")
    print(f"Contains Number: {number}")
    print(f"Contains Special Character: {special}")
    print(f"Common Password: {common}")
    print(f"\nOverall Password Strength: {strength}")

if __name__ == "__main__":
    main()
 

