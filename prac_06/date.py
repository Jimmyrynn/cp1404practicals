from datetime import date, timedelta


class Date:
    """Represents a date object."""

    def __init__(self, day, month, year):
        """Initialise a Date instance"""
        self.date = date(year, month, day)

    def __str__(self):
        """Return a string containing date information DD/MM/YYYY."""
        return self.date.strftime("%d/%m/%Y")

    def add_days(self, n):
        """Add days to current date."""
        new_date = self.date + timedelta(days=n)
        return Date(new_date.day, new_date.month, new_date.year)


def main():
    """Program to calculate future date."""
    amount_of_days = int(input("Enter Amount Of Days: "))
    today = date.today()
    future_date = Date(int(today.strftime("%d")), int(today.strftime("%m")), int(today.strftime("%Y")))
    updated_date = future_date.add_days(amount_of_days)
    print(f"Date after adding {amount_of_days} days:", updated_date)


main()
