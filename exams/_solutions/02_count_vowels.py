def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    # Loop through each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            count += 1

    return count
