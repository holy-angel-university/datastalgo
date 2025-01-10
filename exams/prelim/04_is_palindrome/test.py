from solution import is_palindrome


def test_is_palindrome():
    test_cases = [
        ("A man, a plan, a canal: Panama", True),  # Palindrome
        ("race a car", False),  # Not a palindrome
        ("No lemon, no melon", True),  # Palindrome
        ("Was it a car or a cat I saw?", True),  # Palindrome
        ("12321", True),  # Palindrome (numbers only)
        ("12345", False),  # Not a palindrome
        ("", True),  # Empty string is a palindrome
        ("a", True),  # Single character is a palindrome
        ("ab", False),  # Not a palindrome
        ("Madam, I'm Adam", True),  # Palindrome
    ]

    total_points = 0

    for i, (input_str, expected_output) in enumerate(test_cases):
        result = is_palindrome(input_str)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected {expected_output}, got {result}."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_is_palindrome()
