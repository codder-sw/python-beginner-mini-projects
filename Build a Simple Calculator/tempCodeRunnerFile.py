try:
    a = int(input("Enter a first number :"))
    a = int(input("Enter a second number :"))

    print("what kind of operation do you want to perfom. Press + for addition\nPress - for subtraction\nPress / for Division\nPress * for multiplication")

    O = input("Enter a operation : ")
    match O:
        case "+":
            print(f"The result is : {a + b}")
        case "-":
            print(f"The result is : {a - b}")
        case "*":
            print(f"The result is : {a * b}")
        case "/":
            print(f"The result is : {a / b}")
        case defalut:
           print("There was an error !!")   
        

except Exception as e:
    print("Enter a valid value of a and b ")