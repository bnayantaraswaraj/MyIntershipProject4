def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

def length_converter():
    meters = float(input("Enter length in meters: "))
    feet = meters * 3.28084
    print(f"{meters} meters is equal to {feet:.2f} feet")

def weight_converter():
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms * 2.20462
    print(f"{kilograms} kilograms is equal to {pounds:.2f} pounds")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")

    choice = input("Enter the option number (1/2/3): ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    else:
        print("Invalid option. Please enter 1, 2, or 3.")
