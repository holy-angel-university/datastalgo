def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ""

    for char in s:
        if char.isalnum():
            cleaned += char.lower()

    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]
