from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Program to calculate fare costs from taxis."""
    print("Lets Drive!")
    menu_choice = get_menu_choice()
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill_total = 0

    while menu_choice != 'q':
        if menu_choice == 'c':
            print_taxis(taxis)
            taxi_choice = int(input("Chose Taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid Taxi Choice")

        elif menu_choice == 'd':
            if current_taxi is not None:
                try:
                    drive_distance = int(input("Drive how far? "))
                    current_taxi.drive(drive_distance)
                    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
                    bill_total += current_taxi.get_fare()
                except ValueError:
                    print("Invalid")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid Option")
        print(f"Bill to date: ${bill_total}")
        menu_choice = get_menu_choice()
    print(f"Total trip cost: {bill_total}")
    print_taxis(taxis)


def get_menu_choice():
    """Return user menu choice."""
    menu_choice = input("(q)uit, c)hoose taxi, d)rive)\n>>> ").lower()
    return menu_choice


def print_taxis(taxis):
    """Print taxi from taxis list."""
    for count, taxi in enumerate(taxis):
        print(count, taxi)


main()
