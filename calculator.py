while True:
    print("\n=== Simple Calculator ===")

    num1 = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero!"
    else:
        result = "Invalid operation!"

    print("Result:", result)

    again = input("\nDo you want to calculate again? (y/n): ")
    if again.lower() != 'y':
        print("Goodbye ")
        break

