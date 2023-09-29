"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
numerator = int(input("Enter the numerator: "))
while numerator == 0:
    print("Invalid Numerator")
    numerator = int(input("Enter the numerator: "))

denominator = int(input("Enter the denominator: "))
while denominator == 0:
    print("Invalid Denominator")
    denominator = int(input("Enter the denominator: "))

try:
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# a.
# When the numerator and denominator are not valid numbers (ie -4)

# b.
# When the user attempts to divide by zero.

# c.
# Adding an error checking loop to get a valid number range.
