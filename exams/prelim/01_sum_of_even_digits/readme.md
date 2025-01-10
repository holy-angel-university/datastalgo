# Sum of Even Digits

###### General instructions for all prelim exams can be found [here](../prelim.md).

## Problem Statement

Write a Python function `sum_of_even_digits(number)` that takes an integer number as input and returns the sum of all even digits in the number. If the number does not contain any even digits, return 0.

Example:
> Input: `1234`  
> Output: `6` (because `2 + 4 = 6`)

> Input: `1357`  
> Output: `0` (no even digits)

> Input: `2468`  
> Output: `20` (because `2 + 4 + 6 + 8 = 20`)

## Instructions

1. Implement the function `sum_of_even_digits(number)` in the file `solution.py`.
2. Do not use any external libraries or advanced Python features (e.g., list comprehensions, lambda functions, etc.).
3. Use only the following Python concepts:
   - Variables and Data Types
   - Conditionals
   - Loops
   - Type Casting
4. Test your solution by running `test.py`. The script will automatically check your implementation against 10 test cases.

## Hints

1. Convert the number to a string to easily iterate through its digits.
2. Use a loop to check each digit.
3. Use the modulo operator `%` to determine if a digit is even.
4. Accumulate the sum of even digits in a variable.