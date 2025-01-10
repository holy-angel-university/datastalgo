# Find the Largest Number in a List

###### General instructions for all prelim exams can be found [here](../prelim.md).

## Problem Statement

Write a Python function `find_largest_number(numbers)` that takes a list of integers `numbers` as input and returns the largest number in the list. If the list is empty, return `None`.

Example:

> Input: `[3, 7, 2, 9, 5]`  
> Output: `9`

> Input: `[-1, -5, -3, -2]`  
> Output: `-1`

> Input: `[]`  
> Output: `None` (empty list)

## Instructions

1. Implement the function `find_largest_number(numbers)` in the file `solution.py`.
2. Do not use any external libraries or advanced Python features (e.g., built-in functions like `max()`, list comprehensions, etc.).
3. Use only the following Python concepts:
   - Variables and Data Types
   - Conditionals
   - Loops
   - Type Casting
4. Test your solution by running `test.py`. The script will automatically check your implementation against 10 test cases.

## Hints

1. Initialize a variable to store the largest number.
2. Loop through each number in the list.
3. Use a conditional statement to compare the current number with the largest number found so far.
4. Handle the case where the list is empty by returning `None`.