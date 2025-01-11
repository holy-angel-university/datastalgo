def find_largest_number(numbers):
    # Check if the list is empty
    if len(numbers) == 0:
        return None

    # Initialize a variable to store the largest number
    largest = numbers[0]

    # Loop through each number in the list
    for num in numbers:
        # Check if the current number is larger than the largest found so far
        if num > largest:
            largest = num

    # Return the largest number
    return largest
