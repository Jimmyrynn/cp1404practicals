"""
Prac_09
unreliable_car_test.py
"""
import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes a reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car only if reliable."""
        random_number = random.randint(1, 100)
        if random_number > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
