import random

number_of_picks = int(input("How many picks? "))
for i in range(number_of_picks):
    number_list = []
    for j in range(6):
        random_number = random.randint(1, 100)
        while random_number in number_list:
            random_number = random.randint(1, 100)
        number_list.append(random_number)
    number_list.sort()
    print(" ".join(f"{random_number:2}" for random_number in number_list))
