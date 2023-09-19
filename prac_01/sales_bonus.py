"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

SMALL_BONUS_PERCENTAGE = 0.1
BIG_BONUS_PERCENTAGE = 0.15
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        user_bonus = SMALL_BONUS_PERCENTAGE * sales
        print(f"Bonus: ${user_bonus:.2f} ")
    else:
        user_bonus = BIG_BONUS_PERCENTAGE * sales
        print(f"Bonus: ${user_bonus:.2f} ")
    sales = float(input("Enter sales: $"))
print("ERROR")

