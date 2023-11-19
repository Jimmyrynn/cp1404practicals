"""
Prac_09
silver_service_taxi.py
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flag fall of ${self.flag_fall}"

    def get_fare(self):
        return self.flag_fall + super().get_fare()
