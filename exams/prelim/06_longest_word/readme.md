# Find the Longest Word in a Sentence

###### General instructions for all prelim exams can be found [here](../prelim.md).

## Problem Statement

Write a Python function `longest_word(sentence)` that takes a string `sentence` as input and returns the longest word in the sentence. If there are multiple words with the same longest length, return the first one encountered. Assume that words are separated by spaces and that the sentence contains no punctuation.

Example:

> Input: `"The quick brown fox jumps over the lazy dog"`  
> Output: `"quick"` (because "quick" is the longest word)

> Input: `"Python is fun"`   
> Output: `"Python` (because "Python" is the longest word)

> Input: `"Hello world"`  
> Output: `"Hello"` (all words are of the same length, return the first one)

> Input: `"A B C D E"`  
> Output: `"A"` (all words are of the same length, return the first one)

## Instructions

1. Implement the function `longest_word(sentence)` in the file `solution.py`.
2. Do not use any external libraries or advanced Python features (e.g., built-in functions like `max()`, list comprehensions, etc.).
3. Use only the following Python concepts:
   - Variables and Data Types
   - Conditionals
   - Loops
   - Type Casting
4. Test your solution by running `test.py`. The script will automatically check your implementation against 10 test cases.

## Hints

1. Split the sentence into words using the `split()` method.
2. Initialize a variable to store the longest word and its leng
3. Loop through each word and update the longest word if the current word is longer.
4. Handle edge cases where all words are of the same length.