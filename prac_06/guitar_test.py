"""
Estimate:  30 minutes
Actual:    15 minutes
"""

from prac_06.guitar import Guitar


def test():
    """Run tests."""
    gibson = Guitar("Gibson L-5 CES", "1922", "16035.40")
    another_guitar = Guitar("Jimbson K-9 JIM", "2003", "12")
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 20. Got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


test()
