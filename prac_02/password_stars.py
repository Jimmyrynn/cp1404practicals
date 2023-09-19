"""
CP1404/CP5632 - Practical
Program to get password and print in asterisks
"""


def main():
    """Get password and print."""
    user_password = get_password()
    print_password(user_password)


def get_password():
    """Get valid password."""
    user_password = input("Enter Password: ")
    while len(user_password) < 10:
        print("Invalid")
        user_password = input("Enter Password: ")
    return user_password


def print_password(user_password):
    """Print password in asterisks. """
    print('*' * len(user_password))


main()
