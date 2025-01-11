def longest_word(sentence):
    words = sentence.split()
    if not words:
        return None

    longest = words[0]  # Assume the first word is the longest

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest
