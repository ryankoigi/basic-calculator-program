# Basic Calculator Program

# Get user inputs
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform calculation based on the operation
if operation == "+":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif operation == "-":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif operation == "*":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation entered. Please use +, -, *, or /.")
