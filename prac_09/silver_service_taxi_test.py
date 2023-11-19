"""
Prac_09
silver_service_taxi_test.py
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    car1 = SilverServiceTaxi("Hummer", 100, 2)
    car1.drive(18)
    print(f"Should Get:$48.8, Got:${car1.get_fare()}")
    print(car1.get_fare() + car1.get_fare())


main()
