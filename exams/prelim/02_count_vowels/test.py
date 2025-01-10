from solution import count_vowels


def test_count_vowels():
    test_cases = [
        ("Hello World", 3),  # e, o, o
        ("Python Programming", 4),  # o, o, a, i
        ("Rhythm", 0),  # No vowels
        ("AEIOUaeiou", 10),  # All vowels
        ("12345", 0),  # No vowels
        ("The quick brown fox", 5),  # e, u, i, o, o
        ("Lorem Ipsum", 4),  # o, e, I, u
        ("", 0),  # Empty string
        ("AeIoU", 5),  # All vowels (mixed case)
        ("Coding is fun", 4),  # o, i, i, u
    ]

    total_points = 0

    for i, (input_str, expected_output) in enumerate(test_cases):
        result = count_vowels(input_str)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected {expected_output}, got {result}."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_count_vowels()
