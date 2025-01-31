from solution import number_to_words

def test_number_to_words():
    test_cases = [
        (0, "zero"),
        (5, "five"),
        (21, "twenty-one"),
        (105, "one hundred and five"),
        (123, "one hundred and twenty-three"),
        (2001, "two thousand and one"),
        (1000, "one thousand"),
        (100500, "one hundred thousand five hundred"),
        (123456789, "one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine"),
        (200000001, "two hundred million and one"),
        (1000000, "one million"),
        (205000, "two hundred and five thousand"),
        (100100, "one hundred thousand one hundred"),
        (999999999, "nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine")
    ]

    total_points = 0
    max_points = len(test_cases) * 10

    for i, (input_num, expected) in enumerate(test_cases):
        result = number_to_words(input_num)
        if result == expected:
            print(f"Test case {i+1} passed!")
            total_points += 10
        else:
            print(f"Test case {i+1} failed. Expected: '{expected}', Got: '{result}'")

    print(f"\nTotal points: {total_points}/{max_points}")

if __name__ == "__main__":
    test_number_to_words()