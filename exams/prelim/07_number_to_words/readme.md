# Number to Words

###### General instructions for all special exams can be found [here](../prelim.md).

Write a Python function `number_to_words(num)` that takes an integer `num` (where `0 <= num <= 999,999,999`) as input and returns the English words representation of the number following specific formatting rules.

## Formatting Rules

- **Numbers less than 20**: Return the word directly (e.g., `5` → `"five"`).
- **Numbers between 20 and 99**: Return the word in the format `"twenty-five"`.
- **Numbers between 100 and 999**:
  - If the number is exactly a multiple of 100 (e.g., 200, 500), return `"two hundred"`.
  - Otherwise, include an `"and"` between the hundreds and the tens/units parts (e.g., `123` → `"one hundred and twenty-three"`, `105` → `"one hundred and five"`).
- **Numbers between 1,000 and 999,999**:
  - Break into thousands and remainder. Thousands part follows rules for numbers <1000, followed by `"thousand"`.
  - Append remainder if non-zero. Use "and" only if remainder is <100 (e.g., `2001` → `"two thousand and one"`, `1234` → `"one thousand two hundred and thirty-four"`).
- **Numbers between 1,000,000 and 999,999,999**:
  - Break into millions, thousands, and remainder. Millions part follows rules for numbers <1000, followed by `"million"`.
  - Thousands part follows rules, followed by `"thousand"`.
  - Append remainder if non-zero. Use "and" appropriately between parts where necessary.
- **Zero**: Return `"zero"`.

## Examples

> Input: `123`  
> Output: `"one hundred and twenty-three"`

> Input: `2001`  
> Output: `"two thousand and one"`

> Input: `123456789`  
> Output: `"one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine"`

## Instructions

1. Implement `number_to_words(num)` in `solution.py`.
2. **Do not use any external libraries, dictionaries, or lists.**
3. Use only:
   - Variables, Conditionals, Loops, Type Casting.
4. Ensure correct hyphens, spaces, and "and" usage.
5. Test via `test.py`.

## Hints

- Decompose the number into millions, thousands, and hundreds.
- Use helper logic for repeated patterns (e.g., converting three-digit segments).
- Thoroughly test edge cases (e.g., numbers with zeros between non-zero digits).