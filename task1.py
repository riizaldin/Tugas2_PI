from datetime import datetime, timedelta

def main():
    # Read the number of days from the user
    days = int(input("Enter number of days: "))

    # Get today's date
    today = datetime.now()

    # Calculate the date after the specified number of days
    future_date = today + timedelta(days=days)

    # Format the future date
    formatted_date = future_date.strftime("%A, %B %d, %Y")

    # Print the formatted date
    print("The date {} days from now will be: {}".format(days, formatted_date))

if __name__ == "__main__":
    main()
