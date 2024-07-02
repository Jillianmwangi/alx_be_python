num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            exit()
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
        exit()

print(f"The result is {result}")