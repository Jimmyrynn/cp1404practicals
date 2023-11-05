"""
Estimate:  30 minutes
Actual:    24 minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name, year, cost):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string containing guitar information."""
        return f"{self.name} ({self.year}) : {self.cost}"

    def __lt__(self, other):
        return self.year < other.year

    def get_age(self):
        """Get guitar age."""
        guitar_age = 2023 - int(self.year)
        return guitar_age

    def is_vintage(self):
        """Determine if vintage."""
        if self.get_age() > 50:
            return True
        else:
            return False


def main():
    guitars = []
    print("My guitars!")
    in_file = open("guitars.csv")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    guitars.sort()
    for guitar in guitars:
        print(guitar)


main()
