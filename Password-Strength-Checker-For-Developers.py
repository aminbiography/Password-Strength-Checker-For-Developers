import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Password is too short! It should be at least 8 characters long."

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Password should include at least one uppercase letter."

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Password should include at least one lowercase letter."

    # Check for digits
    if not re.search(r'[0-9]', password):
        return "Password should include at least one digit."

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should include at least one special character."

    return "Password is strong!"

# Example usage
password = input("Enter a password to check: ")
print(check_password_strength(password))
