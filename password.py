import random

vault = {}

def is_password_strong(password, username=""):
    MIN_LENGTH = 12
    if len(password) < MIN_LENGTH:
        return False, "Password must be at least 12 characters long."
    if username and username.lower() in password.lower():
        return False, "Password cannot contain the username."
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    if not all([has_upper, has_lower, has_digit, has_special]):
        return False, "Password must include uppercase, lowercase, number, and special character."
    simple_patterns = ["password", "qwerty", "abc", "123", "letmein", "admin"]
    for pattern in simple_patterns:
        if pattern in password.lower():
            return False, "Password is too common or contains simple patterns."
    return True, "Strong password!"

def check_password_strength(password, username=""):
    ok, msg = is_password_strong(password, username)
    return "Strong" if ok else "Weak (" + msg + ")"

def generate_strong_password(username=""):
    MIN_LENGTH = 12
    upper = [chr(i) for i in range(ord('A'), ord('Z')+1)]
    lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
    digit = [chr(i) for i in range(ord('0'), ord('9')+1)]
    special = list("!@#$%^&*()-_=+,.?")

    while True:
        # Always include at least one from each category
        password_chars = [
            random.choice(upper),
            random.choice(lower),
            random.choice(digit),
            random.choice(special)
        ]
        all_chars = upper + lower + digit + special
        password_chars += [random.choice(all_chars) for _ in range(MIN_LENGTH - 4)]
        random.shuffle(password_chars)
        password = ''.join(password_chars)
        # Check strength against all rules
        strong, _ = is_password_strong(password, username)
        if strong:
            return password

def add_credential():
    username = input("Enter username: ")
    while True:
        print("1. Enter my own password")
        print("2. Generate a strong password for me")
        pw_choice = input("Pick an option (1-2): ")
        if pw_choice == "2":
            password = generate_strong_password(username)
            print("Your generated strong password is:", password)
            print("Remember to save it somewhere safe.")
        elif pw_choice == "1":
            password = input("Enter password: ")
        else:
            print("Invalid choice, try again.")
            continue
        ok, msg = is_password_strong(password, username)
        if ok:
            vault[username] = password
            print("Credential saved!\n")
            break
        else:
            print("Password not strong enough:", msg)
            print("Please try again.\n")

def view_credentials():
    if not vault:
        print("No credentials saved.\n")
        return
    print("\nCredentials stored:")
    for user, pwd in vault.items():
        print("Username:", user, "| Password:", pwd)
    print()

def delete_credential():
    username = input("Enter username to delete: ")
    if username in vault:
        del vault[username]
        print("Credential deleted.\n")
    else:
        print("Username not found.\n")

def analyze_password():
    username = input("Enter username for analysis: ")
    password = input("Enter password to check: ")
    strength = check_password_strength(password, username)
    print("Password strength:", strength)
    if strength == "Strong":
        print("Good job! Your password meets strong standards.\n")
    else:
        print("Review the password requirements and try again.\n")

def generate_and_show_password():
    username = input("Enter username for which to generate password: ")
    password = generate_strong_password(username)
    print("Here is your strong, standards-compliant password:")
    print(password)
    print("Save it somewhere safe!\n")

def main_menu():
    while True:
        print("----- Secure Password Vault -----")
        print("1. Add new credential")
        print("2. View all credentials")
        print("3. Delete a credential")
        print("4. Check password strength")
        print("5. Generate a strong password")
        print("6. Exit")
        choice = input("Pick an option (1-6): ")
        print()
        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            delete_credential()
        elif choice == "4":
            analyze_password()
        elif choice == "5":
            generate_and_show_password()
        elif choice == "6":
            print("Goodbye! Always use strong, unique passwords.")
            break
        else:
            print("Please enter a valid option (1-6).\n")

if __name__ == "__main__":
    main_menu()
