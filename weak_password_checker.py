# List of common weak passwords
COMMON_WEAK_PASSWORDS = [
    '123456', 'password', '12345678', 'qwerty', '123456789', '12345', '1234', '111111',
    '1234567', 'dragon', '123123', 'letmein', 'password1', 'admin', 'welcome'
]

def check_weak_passwords(passwords):
    """
    Checks a list of passwords against a list of common weak passwords.

    Args:
    passwords (list): List of passwords to check.

    Returns:
    list: List of weak passwords found.
    """
    weak_passwords = [password for password in passwords if password in COMMON_WEAK_PASSWORDS]
    return weak_passwords

def read_passwords_from_file(file_path):
    """
    Reads passwords from a file.

    Args:
    file_path (str): Path to the file containing passwords.

    Returns:
    list: List of passwords read from the file.
    """
    with open(file_path, 'r') as file:
        passwords = file.read().splitlines()
    return passwords

def main():
    """
    Main function to read passwords from a file and check for weak passwords.
    """
    file_path = input("Enter the path to the file containing passwords: ")
    try:
        passwords = read_passwords_from_file(file_path)
        weak_passwords = check_weak_passwords(passwords)
        if weak_passwords:
            print(f"Weak passwords found: {weak_passwords}")
        else:
            print("No weak passwords found.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")

if __name__ == "__main__":
    main()

