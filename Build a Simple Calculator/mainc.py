# Using try block to catch invalid input errors (like text instead of numbers)
try:
    # Taking first number input from the user and converting to integer
    a = int(input("Enter the first number: "))
    
    # Taking second number input from the user and converting to integer
    b = int(input("Enter the second number: "))

    # Showing user the available math operations
    print("What operation do you want to perform?")
    print("Press + for Addition")
    print("Press - for Subtraction")
    print("Press * for Multiplication")
    print("Press / for Division")

    # Taking operator input from user (+, -, *, /)
    O = input("Enter an operation: ")

    # match-case structure (Python 3.10+) — works like switch-case
    match O:

        # If user enters +
        case "+":
            print(f"The result is : {a + b}")

        # If user enters -
        case "-":
            print(f"The result is : {a - b}")

        # If user enters *
        case "*":
            print(f"The result is : {a * b}")

        # If user enters /
        case "/":
            # Special check: Avoid division by zero
            if b == 0:
               print("Division by zero not allowed")
            else:
               print(f"The result is: {a / b}")

        # If user enters anything else (default case)
        case _:
            print("Invalid operation !!")

# except block runs when the user input is not a valid number
except Exception as e:
    print("Enter a valid numeric value for a and b.")
