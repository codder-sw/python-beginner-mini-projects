try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What operation do you want to perform?")
    print("Press + for Addition")
    print("Press - for Subtraction")
    print("Press * for Multiplication")
    print("Press / for Division")

    O = input("Enter an operation: ")

    match O:
        case "+":
            print(f"The result is : {a + b}")
        case "-":
            print(f"The result is : {a - b}")
        case "*":
            print(f"The result is : {a * b}")
        case "/":
            if b == 0:
               print("Division by zero not allowed")
            else:
               print(f"The result is: {a / b}")

        case _:
            print("Invalid operation !!")

except Exception as e:
    print("Enter a valid numeric value for a and b.")
