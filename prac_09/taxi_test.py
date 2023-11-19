"""
Prac_09
taxi_test.py
"""

from prac_09.taxi import Taxi


def main():
    """Testing code."""
    car1 = Taxi("Prius 1", 100)
    car1.drive(40)
    print(car1)
    print(car1.get_fare())
    car1.start_fare()
    car1.drive(100)
    print(car1)
    print(car1.get_fare())


main()
