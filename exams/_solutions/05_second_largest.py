def find_second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    # If second_largest is still -inf, it means there are no two unique numbers
    if second_largest == float("-inf"):
        return None

    return second_largest
