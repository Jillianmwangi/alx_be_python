import datetime

def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days_to_add):
    current_date = datetime.datetime.now().date()
    future_date = current_date + datetime.timedelta(days=days_to_add)
    print(f"Future Date (after {days_to_add} days): {future_date}")

def main():
    display_current_datetime()
    days_to_add = int(input("Enter the number of days to add: "))
    calculate_future_date(days_to_add)

if __name__ == "__main__":
    main()