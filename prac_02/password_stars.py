user_password = input("Enter Password: ")
while len(user_password) < 10:
    print("Invalid")
    user_password = input("Enter Password: ")
print('*' * len(user_password))
