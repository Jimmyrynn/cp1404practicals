def main():
    """Prompts the user for 5 numbers, stores each in a list, then outputs information."""
    list_of_numbers = []
    authorised_users = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye']
    username = input("Username: ")
    if username in authorised_users:
        print("Access granted")
        for i in range(1, 6):
            user_input = int(input(f"Number {i}: "))
            list_of_numbers.append(user_input)
        print_results(list_of_numbers)
    else:
        print("Access denied")


def print_results(list_of_numbers):
    """Print results."""
    print(f"The first number is {list_of_numbers[0]}")
    print(f"The last number is {list_of_numbers[-1]}")
    print(f"The smallest number is {min(list_of_numbers)}")
    print(f"The smallest number is {max(list_of_numbers)}")
    print(f"The average of the numbers is {(sum(list_of_numbers) / len(list_of_numbers)):.1f}")


main()
