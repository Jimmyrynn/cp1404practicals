"""
Word Occurrences
Estimate: 30 minutes
Actual:  35 minutes
"""


def main():
    """Print names from user emails."""
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != '':
        name = get_name_from_email(user_email)
        valid_selection = input(f"Is your name {name.title()} (Y/n) ").lower()
        if valid_selection != 'y' and valid_selection != "":
            name = input("Name: ")
        email_to_name[user_email] = name
        user_email = input("Email: ")
    for user_email, name in email_to_name.items():
        print(f"{name} ({user_email})")


def get_name_from_email(user_email):
    """Extract name from email."""
    email_username = user_email.split('@')[0]
    parts = email_username.split('.')
    name = " ".join(parts)
    return name


main()
