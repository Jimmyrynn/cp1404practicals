total_price = 0
DISCOUNT_PERCENTAGE = 0.1
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid Number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    total_price = item_price + total_price
if total_price > 100:
    discounted_price = total_price - (total_price * DISCOUNT_PERCENTAGE)
    print(f"Total price for {number_of_items} items is ${discounted_price:.2f}")
else:
    print(f"Total price for {number_of_items} is ${total_price}")
