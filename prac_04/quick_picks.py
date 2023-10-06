import random
AMOUNT_OF_NUMBERS = 6
RANDOM_NUMBER_MINIMUM = 1
RANDOM_NUMBER_MAXIMUM = 45

number_of_picks = int(input("How many picks? "))
for i in range(number_of_picks):
    number_list = []
    for j in range(AMOUNT_OF_NUMBERS):
        random_number = random.randint(RANDOM_NUMBER_MINIMUM, RANDOM_NUMBER_MAXIMUM)
        while random_number in number_list:
            random_number = random.randint(RANDOM_NUMBER_MINIMUM, RANDOM_NUMBER_MAXIMUM)
        number_list.append(random_number)
    number_list.sort()
    print(" ".join(f"{random_number:2}" for random_number in number_list))
