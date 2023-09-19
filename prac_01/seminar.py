# Example 1
# number_of_gifts = int(input("Number of gifts: "))
# number_of_students = int(input("Number of students: "))
# number_of_gifts_per_student = number_of_gifts // number_of_students
# number_of_gifts_left_over = number_of_gifts % number_of_students
# print(number_of_gifts_per_student, number_of_gifts_left_over)

# Example 2
item_price = float(input("Enter Item Price: "))
include_gst = input("Does Item Have GST: ").lower()
if include_gst == 'y':
    gst_total = item_price * 0.10
    total_price = item_price + gst_total
    print(f"${total_price:.2f}")
else:
    print(f"${item_price}")
