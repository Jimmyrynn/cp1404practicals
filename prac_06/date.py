from datetime import date, timedelta


class Date:
    def __init__(self, day, month, year):
        self.date = date(year, month, day)

    def __str__(self):
        return self.date.strftime("%m/%d/%Y")

    def add_days(self, n):
        new_date = self.date + timedelta(days=n)
        return Date(new_date.day, new_date.month, new_date.year)


def main():
    amount_of_days = int(input("Enter Amount Of Days: "))
    today = date.today()
    future_date = Date(int(today.strftime("%d")), int(today.strftime("%m")), int(today.strftime("%Y")))
    updated_date = future_date.add_days(amount_of_days)
    print(f"Date after adding {amount_of_days} days:", updated_date)


main()
