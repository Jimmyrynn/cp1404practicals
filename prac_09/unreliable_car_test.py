"""
Prac_09
unreliable_car_test.py
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Testing code."""
    car1 = UnreliableCar("Prius 1", 20, 50)
    car1.drive(100)
    print(car1)


main()
