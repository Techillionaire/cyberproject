import re

def is_strong_password(password):
    # Check the length (at least 8 characters)
    if len(password) < 8:
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}":;<>,.?~]', password):
        return False

    return True

def main():
    password = input("Enter a password: ")
    
    if is_strong_password(password):
        print("This is a strong password!")
    else:
        print("This password is weak. Please choose a stronger password.")

if __name__ == "__main__":
    main()