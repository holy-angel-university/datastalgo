# Check if a String is a Palindrome

###### General instructions for all prelim exams can be found [here](../prelim.md).

## Problem Statement

Write a Python function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome, and `False` otherwise. A palindrome is a string that reads the same backward as forward. Ignore case and non-alphanumeric characters.

Example:

> Input: `"A man, a plan, a canal: Panama"`  
> Output: `True` (because it reads the same backward when ignoring case and non-alphanumeric characters)

> Input: `"race a car"`   
> Output: `False` (because it does not read the same backward)

> Input: `"No lemon, no melon"`  
> Output: `True` (because it reads the same backward when ignoring case and non-alphanumeric characters)

## Instructions

1. Implement the function `is_palindrome(s)` in the file `solution.py`.
2. Do not use any external libraries or advanced Python features (e.g., regular expressions, list comprehensions, etc.).
3. Use only the following Python concepts:
   - Variables and Data Types
   - Conditionals
   - Loops
   - Type Casting
4. Test your solution by running `test.py`. The script will automatically check your implementation against 10 test cases.

## Hints

1. Remove non-alphanumeric characters and convert the string to lowercase.
2. Compare the string with its reverse.
3. Use a loop or string slicing to reverse the string.