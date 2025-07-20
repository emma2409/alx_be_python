num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
        print("The result  is {result}")
    case "-":
        result = num1 - num2
        print("The result  is {result}")
    case "*":
        result = num1 * num2
        print("The result  is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print("The result  is {result}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation.")

# This code implements a simple calculator using match-case statements.
# It prompts the user for two numbers and an operation, then performs the operation and prints the result.
# The match-case structure allows for clear and concise handling of different operations.       
# The code handles division by zero and provides an error message for invalid operations.
# The code uses Python's match-case feature introduced in Python 3.10 for cleaner syntax.
