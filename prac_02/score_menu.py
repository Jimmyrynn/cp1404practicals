def main():
    """Determine grade from a valid score and print stars."""
    print("Menu:\n(G)et\n(P)rint\n(S)how\n(Q)uit")
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == 'g':
            user_score = get_valid_score()
        elif user_choice == 'p':
            grade_score(user_score)
            print(f"{ grade_score(user_score)}")
        elif user_choice == 's':
            print('*' * user_score)
        else:
            print("Invalid")
        print("Menu:\n(G)et\n(P)rint\n(S)how\n(Q)uit")
        user_choice = input(">>> ").lower()
    print("Goodbye!")


def get_valid_score():
    """Get a valid score from the user."""
    user_score = int(input("Enter Score: "))
    while 0 < user_score > 100:
        print("Invalid")
        user_score = input("Enter Score: ")
    return user_score


def grade_score(user_score):
    """Grade the user score."""
    if user_score > 100:
        return "Invalid Score"
    elif user_score >= 90:
        return "Excellent"
    elif user_score >= 50:
        return "Passable"
    elif user_score < 50:
        return "Bad"
    else:
        return "Invalid score"


main()
