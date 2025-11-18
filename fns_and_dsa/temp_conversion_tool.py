# this script 'temp_conversion_tool.py' converts from celcius to fahrenheit and vice-versa

# Define Global Conversion Factors, factors are defined once and read by the functions
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit: float) -> float:
    """Converts a temperature from Fahrenheit to Celsius using a global factor."""
    # Formula: C = (F - 32) * (5/9)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """Converts a temperature from Celsius to Fahrenheit using a global factor."""
    # Formula: F = C * (9/5) + 32
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # --- Input and Validation ---
    while True:
            temp_input = input("Enter the temperature to convert: ")
            try:
                temperature = float(temp_input)
                break # exit loop if conversion to float is successful
            except ValueError:
                print("Invalid temperature. Please enter a numeric value.")

    # Get the unit and normalize the input
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ('C', 'F'):
            break
        print("Invalid unit entered. Please use 'C' or 'F'.")

    # final conversion of value
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp:.2f}°C")
    else:
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp:.2f}°F")

if __name__ == "__main__":
    main()

