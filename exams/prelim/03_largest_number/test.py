from solution import find_largest_number


def test_find_largest_number():
    test_cases = [
        ([3, 7, 2, 9, 5], 9),  # Largest is 9
        ([-1, -5, -3, -2], -1),  # Largest is -1
        ([], None),  # Empty list
        ([10], 10),  # Single element
        ([1, 1, 1, 1], 1),  # All elements are the same
        ([0, 0, 0, 0], 0),  # All elements are zero
        ([5, 3, 8, 1, 8], 8),  # Largest is 8 (appears twice)
        ([-10, -20, -30, -40], -10),  # Largest is -10
        ([100, 200, 300, 400], 400),  # Largest is 400
        ([2, 4, 6, 8, 10, 12], 12),  # Largest is 12
    ]

    total_points = 0

    for i, (input_list, expected_output) in enumerate(test_cases):
        result = find_largest_number(input_list)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected {expected_output}, got {result}."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_find_largest_number()
