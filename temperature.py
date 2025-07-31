"""Utility functions for temperature conversion."""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit temperature to Celsius."""
    return (fahrenheit - 32) * 5/9

if __name__ == "__main__":
    # Example usage
    temp_c = 0


    choice = input(
        "Convert (C)elsius to Fahrenheit or (F)ahrenheit to Celsius? "
    ).strip().upper()

    if choice == "C":
        while True:
            value_str = input("Enter temperature in Celsius: ")
            try:
                value = float(value_str)
                break
            except ValueError:
                print("Please enter a valid number.")
        result = celsius_to_fahrenheit(value)

    elif choice == "F":
        while True:
            value_str = input("Enter temperature in Fahrenheit: ")
            try:
                value = float(value_str)
                break
            except ValueError:
                print("Please enter a valid number.")
        result = fahrenheit_to_celsius(value)

    else:
        print("Invalid option. Use 'C' or 'F'.")
