from solution import sum_of_even_digits


def test_sum_of_even_digits():
    test_cases = [
        (1234, 6),
        (1357, 0),
        (2468, 20),
        (0, 0),
        (1111, 0),
        (2222, 8),
        (8642, 20),
        (123456789, 20),
        (987654321, 20),
        (1020304050, 6),
    ]

    total_points = 0

    for i, (input_num, expected_output) in enumerate(test_cases):
        result = sum_of_even_digits(input_num)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected {expected_output}, got {result}."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_sum_of_even_digits()
