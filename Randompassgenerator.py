import random
import string

def generate_password(length):
    # Define the possible characters in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    # Ask the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
