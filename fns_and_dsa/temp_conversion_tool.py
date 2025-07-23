# FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
# CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

# def convert_to_celsius(temperature):
#     """Converting Fahrenheit to Celsius."""
#     global FAHRENHEIT_TO_CELSIUS_FACTOR
#     if temperature < -459.67:
#         raise ValueError("Temperature below absolute zero is not allowed.")
#     print(f"{temperature}°F is {(temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

# def convert_to_fahrenheit(temperature):
#     """Converting Celsius to Fahrenheit."""
#     global CELSIUS_TO_FAHRENHEIT_FACTOR
#     if temperature < -273.15:
#         raise ValueError("Temperature below absolute zero is not allowed.")
#     print(f"{temperature}°C is {(temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32}°F")

# def main():
#     """Main function to run the temperature conversion tool."""
#     temperature = float(input("Enter the temperature to convert: "))
#     question = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

#     match question:
#         case "C":
#             convert_to_fahrenheit(temperature)
#         case "F":
#             convert_to_celsius(temperature)
#         case _:
#             print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# main()

# ==========================================

# Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using a global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using a global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)  # Convert to float to validate numeric input

        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Perform the correct conversion
        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()

