"""
Estimate:  30 minutes
Actual:    22 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Format user input and determine if guitar is vintage."""
    print("My guitars!")
    user_guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = input("Year: ")
        guitar_cost = input("Cost: ")
        user_guitars.append(Guitar(guitar_name, guitar_year, guitar_cost))
        guitar_name = input("Name: ")
    user_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    user_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("...snip...")
    print("These are my guitars: ")
    for i, guitar in enumerate(user_guitars, 1):
        category = "(vintage)" if guitar.get_age() >= 50 else " "
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10.2f} {category}")


main()
