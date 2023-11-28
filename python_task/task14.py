def add_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is: {result}")
            break
        except ValueError:
            print("Invalid character entered. Please enter numbers or floats only.")
            # Clear the input buffer
            input()

# Call the function to add numbers
add_numbers()