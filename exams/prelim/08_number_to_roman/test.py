from solution import number_to_roman


def test_number_to_roman():
    test_cases = [
        (3, "III"),  # Smallest number
        (58, "LVIII"),  # Number with additive notation
        (1994, "MCMXCIV"),  # Number with subtractive notation
        (3999, "MMMCMXCIX"),  # Largest valid number
        (1, "I"),  # Smallest valid number
        (10, "X"),  # Simple case
        (40, "XL"),  # Subtractive notation
        (99, "XCIX"),  # Subtractive notation
        (444, "CDXLIV"),  # Multiple subtractive notations
        (2023, "MMXXIII"),  # Sample year
    ]

    total_points = 0

    for i, (input_num, expected_output) in enumerate(test_cases):
        result = number_to_roman(input_num)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += (
                10  # Each test case is worth 10 points (100 / 10 test cases)
            )
        else:
            print(
                f"Test case {i + 1} failed. Expected '{expected_output}', got '{result}'."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_number_to_roman()
