def sum_of_even_digits(number):
    # Convert the number to a string to iterate through digits
    number_str = str(number)
    total = 0

    # Loop through each character in the string
    for digit_char in number_str:
        # Convert the character back to an integer
        digit = int(digit_char)
        # Check if the digit is even
        if digit % 2 == 0:
            total += digit

    return total
