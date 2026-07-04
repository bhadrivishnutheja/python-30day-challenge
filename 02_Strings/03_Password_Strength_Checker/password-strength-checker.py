# Password Strength Checker
def check_password_strength(password):
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any( char in "!@#$%^&*()_+-=[]{}|;:,.<>?" for char in password)

    strength = sum([length, has_upper, has_lower, has_digit, has_special])

    return {
        'length': length,
        'uppercase': has_upper,
        'lowercase': has_lower,
        'digit': has_digit,
        'special': has_special,
        'strength': strength
    }

def display_strength(result):
    print("\n --- Password Strength Analysis ----")
    print(f"Length >= 8: {'✓'if result['length'] else '✗'}")
    print(f" Has uppercase: { '✓' if result['uppercase'] else '✗'}")
    print(f" Has lowercase: { '✓' if result['lowercase'] else '✗'}")
    print(f" Has digit: { '✓' if result['digit'] else '✗'}")
    print(f" Has special character: { '✓' if result['special'] else '✗'}")

    strength = result['strength']
    if strength == 5:
        print("Strength: Very Strong 💪")
    elif strength == 4:
        print("Strength: Strong 👍")
    elif strength == 3:
        print("Strength: Medium ⚠️")
    else:
        print("Strength: Weak ❌")
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    display_strength(result)