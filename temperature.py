"""Utility functions for temperature conversion."""

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return celsius * 9/5 + 32

if __name__ == "__main__":
    # Example usage
    temp_c = 0
    print(f"{temp_c} °C = {celsius_to_fahrenheit(temp_c)} °F")
