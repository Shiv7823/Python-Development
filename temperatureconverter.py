def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def main():
    print("Temperature Converter")
    
    while True:
        print("Choose the conversion direction:")
        print("1. Fahrenheit to Celsius")
        print("2. Celsius to Fahrenheit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        if choice == '1':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif choice == '2':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
        next_conversion = input("Do you want to perform another conversion? (yes/no): ")
        if next_conversion.lower() != 'yes':
            break
    
    print("Thank you for using the temperature converter!")

if __name__ == "__main__":
    main()
