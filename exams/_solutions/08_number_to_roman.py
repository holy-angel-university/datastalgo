def number_to_roman(num):
    roman = ''
    
    # Thousands place
    thousands = num // 1000
    roman += 'M' * thousands
    remainder = num % 1000
    
    # Hundreds place
    hundreds = remainder // 100
    if hundreds == 9:
        roman += 'CM'
    elif hundreds >= 5:
        roman += 'D' + 'C' * (hundreds - 5)
    elif hundreds == 4:
        roman += 'CD'
    else:
        roman += 'C' * hundreds
    remainder %= 100
    
    # Tens place
    tens = remainder // 10
    if tens == 9:
        roman += 'XC'
    elif tens >= 5:
        roman += 'L' + 'X' * (tens - 5)
    elif tens == 4:
        roman += 'XL'
    else:
        roman += 'X' * tens
    remainder %= 10
    
    # Ones place
    ones = remainder
    if ones == 9:
        roman += 'IX'
    elif ones >= 5:
        roman += 'V' + 'I' * (ones - 5)
    elif ones == 4:
        roman += 'IV'
    else:
        roman += 'I' * ones
    
    return roman