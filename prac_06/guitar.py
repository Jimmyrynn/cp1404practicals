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
