def simple_calculator():
    print("Welcome to the Simple Calculator!")
    print("Please choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # :: Dictionary to map choices to operations
    operations = {
        1: ("Addition", lambda x, y: x + y),
        2: ("Subtraction", lambda x, y: x - y),
        3: ("Multiplication", lambda x, y: x * y),
        4: (
            "Division",
            lambda x, y: x / y if y != 0 else "Error: Division by zero is not allowed.",
        ),
    }

    # :: Prompt the user to choose an operation
    while True:
        try:
            choice = int(input("Enter the number of your choice (1-4): "))
            if choice not in operations:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

    # :: Prompt the user to input two numbers
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    # :: Perform the selected operation and display the result
    operation_name, operation_func = operations[choice]
    result = operation_func(num1, num2)

    if isinstance(result, str):
        print(result)
    else:
        print(f"The result of {operation_name} is: {result}")


if __name__ == "__main__":
    simple_calculator()
