# Simple Calculator 

This Python script implements a simple calculator that allows the user to perform basic arithmetic operations: addition, subtraction, multiplication, and division. The user is prompted to choose an operation and input two numbers. The result of the operation is then displayed.

## Functions

`simple_calculator()`

- This is the main function that runs the simple calculator. It handles user input for the operation and numbers, performs the selected operation, and displays the result.

## Calculator Flow

1. **Welcome Message**: The calculator starts with a welcome message.
2. **Choose Operation**: The user is prompted to choose an operation from the following options:

   - Addition
   - Subtraction
   - Multiplication
   - Division

3. **Validate Operation Choice**: The user's choice is validated to ensure it is a number between 1 and 4. If the input is invalid, the user is prompted to enter a valid choice.

4. **Input Numbers**: The user is prompted to input two numbers. The input is validated to ensure they are valid numbers. If the input is invalid, the user is prompted to enter valid numbers.

5. **Perform Operation**: The selected operation is performed on the two numbers. If the operation is division and the second number is zero, an error message is displayed indicating division by zero is not allowed.
   
6. **Display Result**: The result of the operation is displayed. If the operation was division and the second number was zero, the error message is displayed instead of the result.

## Example Output

```shell
Welcome to the Simple Calculator!
Please choose an operation:
1. Addition
2. Subtraction
3. Multiplication
4. Division
Enter the number of your choice (1-4): 1
Enter the first number: 5
Enter the second number: 3
The result of Addition is: 8.0
```

## Running the Calculator

To run the calculator, execute the script. The calculator will start automatically if the script is run directly:

```shell
python main.py
```