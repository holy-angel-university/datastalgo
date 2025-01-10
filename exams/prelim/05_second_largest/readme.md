# Find the Second Largest Number in a List

###### General instructions for all prelim exams can be found [here](../prelim.md).

## Problem Statement

Write a Python function `find_second_largest(numbers)` that takes a list of integers `numbers` as input and returns the second largest number in the list. If the list has fewer than two unique numbers, return `None`.

Example:

> Input: `[3, 7, 2, 9, 5]`  
> Output: `7` (because `9` is the largest and `7` is the second largest)

> Input: `[-1, -5, -3, -2]`   
> Output: `-2` (because `-1` is the largest and `-2` is the second largest)

> Input: `[5, 5, 5, 5]`  
> Output: `None` (because there are no two unique numbers)

> Input: `[10]`  
> Output: `None` (because there is only one number)

## Instructions

1. Implement the function `find_second_largest(numbers)` in the file `solution.py`.
2. Do not use any external libraries or advanced Python features (e.g., built-in functions like `sorted()`, `set()`, etc.).
3. Use only the following Python concepts:
   - Variables and Data Types
   - Conditionals
   - Loops
   - Type Casting
4. Test your solution by running `test.py`. The script will automatically check your implementation against 10 test cases.

## Hints

1. Initialize two variables to store the largest and second largest numbers.
2. Loop through each number in the list and update the largest and second largest numbers accordingly.
3. Handle edge cases where the list has fewer than two unique numbers.