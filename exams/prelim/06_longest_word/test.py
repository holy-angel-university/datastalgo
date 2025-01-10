from solution import longest_word


def test_longest_word():
    test_cases = [
        ("The quick brown fox jumps over the lazy dog", "quick"),  # Longest is "quick"
        ("Hello world", "Hello"),  # All words are of the same
        ("Python is fun", "Python"),  # Longest is "Python"
        ("A B C D E", "A"),  # All words are of the same length, return the first one
        ("", None),  # Empty sentence
        ("One", "One"),  # Single word
        ("The cat in the hat", "The"),  # Longest is "The" (first encountered)
        ("This is a test sentence", "sentence"),  # Longest is "sentence"
        (
            "Longest word in this sentence is longest",
            "sentence",
        ),  # Longest is "sentence"
        ("Short words only", "Short"),  # Longest is "words"
    ]

    total_points = 0

    for i, (input_sentence, expected_output) in enumerate(test_cases):
        result = longest_word(input_sentence)
        if result == expected_output:
            print(f"Test case {i + 1} passed!")
            total_points += 10
        else:
            print(
                f"Test case {i + 1} failed. Expected {expected_output}, got {result}."
            )

    print(f"\nTotal points: {total_points} / 100")


if __name__ == "__main__":
    test_longest_word()
