def main():
    print("Menu:\n(G)et\n(P)rint\n(S)how\n(Q)uit")
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == 'g':
            get_valid_score(user_choice)
        elif user_choice == 'p':
            print("P")
        elif user_choice == 's':
            print("S")
        else:
            print("Invalid")
        print("Menu:\n(G)et\n(P)rint\n(S)how\n(Q)uit")
        user_choice = input(">>> ").lower()
    print("Goodbye!")


def get_valid_score(user_choice):
    while 0 > user_choice > 100:
        print("Invalid")
        user_choice = input(">>> ").lower()


main()
