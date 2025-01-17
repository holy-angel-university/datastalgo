from solution import number_to_words


def test_number_to_words():
    test_cases = [
        (0, "zero"),  # Edge case: zero
        (5, "five"),  # Single-digit number
        (12, "twelve"),  # Number in the teens
        (123, "one hundred twenty-three"),  # Number with hundreds, tens, and units
        (1000, "one thousand"),  # Number with a thousands place
        (
            1234,
            "one thousand two hundred thirty-four",
        ),  # Number with thousands, hundreds, tens, and units
        (9999, "nine thousand nine hundred ninety-nine"),  # Largest 4-digit number
        (1111, "one thousand one hundred eleven"),  # All digits are the same
        (
            2000,
            "two thousand",
        ),  # Number with zeros in the hundreds, tens, and units places
        (999, "nine hundred ninety-nine"),  # Largest 3-digit number
    ]

    total_points = 0

    for i, (input_num, expected_output) in enumerate(test_cases):
        result = number_to_words(input_num)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected '{expected_output}', got '{result}'."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_number_to_words()
