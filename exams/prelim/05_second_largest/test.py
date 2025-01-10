from solution import find_second_largest


def test_find_second_largest():
    test_cases = [
        ([3, 7, 2, 9, 5], 7),  # Second largest is 7
        ([-1, -5, -3, -2], -2),  # Second largest is -2
        ([5, 5, 5, 5], None),  # No second largest
        ([10], None),  # Only one number
        ([1, 2, 3, 4, 5], 4),  # Second largest is 4
        ([5, 1, 5, 3, 5], 3),  # Second largest is 3
        ([100, 200, 300, 400], 300),  # Second largest is 300
        ([0, 0, 0, 0], None),  # All elements are the same
        ([2, 4, 6, 8, 10, 12], 10),  # Second largest is 10
        ([12, 12, 12, 6, 6, 6], 6),  # Second largest is 6
    ]

    total_points = 0

    for i, (input_list, expected_output) in enumerate(test_cases):
        result = find_second_largest(input_list)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected {expected_output}, got {result}."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_find_second_largest()
