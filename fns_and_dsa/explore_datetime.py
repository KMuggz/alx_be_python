# this script 'explore_datetime.py' will take a int-value and add that number of days from current date

from datetime import datetime, timedelta

def display_current_datetime() -> datetime:
    """
    Gets and prints the current date and time in a specific format.

    Returns:
        datetime: the current date and time as a datetime object.
    """

    # Part 1: Display the Current Date and Time
    current_date = datetime.now()
    
    # Format: "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nCurrent date and time: {formatted_datetime}")
    
    # Returns the current_date object for potential reuse
    return current_date

def calculate_future_date(current_date: datetime) -> None:
    """
    Prompts the user for days to add and calculates the future date.

    Args:
        current_date: A datetime object representing the starting date.
    """
    # Part 2: Calculate a Future Date
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for the number of days.")

    # Calculate the future date using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format: "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")


def main():
    current_datetime_obj = display_current_datetime()
    calculate_future_date(current_datetime_obj)

if __name__ == "__main__":
    main()
