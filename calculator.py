# Get two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Check if inputs are numbers
if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)

    # Ask for operation
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the corresponding operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:  # Avoid division by zero
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    print("Result:", result)
else:
    print("Invalid input! Please enter numeric values.")
