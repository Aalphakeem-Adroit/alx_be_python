FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)

def convert_to_celsius(temperature):
    """Converting Fahrenheit to Celsius."""
    if temperature < -459.67:
        raise ValueError("Temperature below absolute zero is not allowed.")
    print(f"{temperature}°F is {(temperature - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

def convert_to_fahrenheit(temperature):
    """Converting Celsius to Fahrenheit."""
    if temperature < -273.15:
        raise ValueError("Temperature below absolute zero is not allowed.")
    print(f"{temperature}°C is {(temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32}°F")

def main():
    """Main function to run the temperature conversion tool."""
    temperature = float(input("Enter the temperature to convert: "))
    question = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    match question:
        case "C":
            convert_to_fahrenheit(temperature)
        case "F":
            convert_to_celsius(temperature)
        case _:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

main()
