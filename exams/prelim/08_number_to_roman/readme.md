# Number to Roman

###### General instructions for all prelim exams can be found [here](../prelim.md).

## Problem Statement

Write a Python function `number_to_roman(num)` that takes an integer `num` (where `1 <= num <= 3999)` as input and returns the Roman numeral representation of the number.

Roman Numeral Rules:

1. Roman numerals are represented by the following symbols:

    - `I` (1)
    - `V` (5)
    - `X` (10)
    - `L` (50)
    - `C` (100)
    - `D` (500)
    - `M` (1000)

2. Symbols are combined to represent numbers. For example:

    - `II` represents `2`.
    - `VI` represents `6`.
    - `IV` represents `4` (one less than `5`).

3. Subtractive notation is used for numbers like 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`), and 900 (`CM`).

Example: 
>Input: `3`  
> Output: "`III`"

> Input: `58`  
> Output: "`LVIII`" 

> Input: `1994`  
> Output: "`MCMXCIV`" 

> Input: `3999`  
> Output: "`MMMCMXCIX`" 

## Instructions

1. Implement the function `palindrome_with_twist(num)` in the file `solution.py`.
2. Do not use any external libraries or advanced Python features (e.g., dictionaries, list comprehensions, etc.).
3. Use only the following Python concepts:
   - Variables and Data Types
   - Conditionals
   - Loops
   - Type Casting
4. Test your solution by running `test.py`. The script will automatically check your implementation against 10 test cases.

## Hints

1. Break the problem into smaller parts:
    - Handle thousands place (1000–3999).
    - Handle hundreds place (100–999).
    - Handle tens place (10–99).
    - Handle ones place (1–9).
2. Use conditionals to determine the range of the number.
3. Use loops and type casting to extract digits and construct the Roman numeral representation.
4. Pay attention to edge cases, such as `0` and numbers with trailing zeros (e.g., `100`, `1000`).