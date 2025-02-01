def number_to_words(num):
    if num == 0:
        return "zero"
    
    result = []
    
    def convert_less_than_thousand(n):
        part = []
        hundreds = n // 100
        remainder = n % 100
        
        if hundreds > 0:
            part.append(get_hundred_word(hundreds))
            if remainder > 0:
                part.append("and")
        
        if remainder > 0:
            if remainder < 20:
                part.append(get_under_twenty(remainder))
            else:
                tens = (remainder // 10) * 10
                units = remainder % 10
                if units == 0:
                    part.append(get_tens(tens))
                else:
                    part.append(f"{get_tens(tens)}-{get_under_twenty(units)}")
        
        return ' '.join(part).strip()
    
    def get_under_twenty(n):
        if n == 1: return "one"
        elif n == 2: return "two"
        elif n == 3: return "three"
        elif n == 4: return "four"
        elif n == 5: return "five"
        elif n == 6: return "six"
        elif n == 7: return "seven"
        elif n == 8: return "eight"
        elif n == 9: return "nine"
        elif n == 10: return "ten"
        elif n == 11: return "eleven"
        elif n == 12: return "twelve"
        elif n == 13: return "thirteen"
        elif n == 14: return "fourteen"
        elif n == 15: return "fifteen"
        elif n == 16: return "sixteen"
        elif n == 17: return "seventeen"
        elif n == 18: return "eighteen"
        elif n == 19: return "nineteen"
        return ""
    
    def get_tens(n):
        if n == 20: return "twenty"
        elif n == 30: return "thirty"
        elif n == 40: return "forty"
        elif n == 50: return "fifty"
        elif n == 60: return "sixty"
        elif n == 70: return "seventy"
        elif n == 80: return "eighty"
        elif n == 90: return "ninety"
        return ""
    
    def get_hundred_word(n):
        return f"{get_under_twenty(n)} hundred"
    
    millions = num // 1_000_000
    thousands_remainder = num % 1_000_000
    thousands = thousands_remainder // 1000
    remainder = thousands_remainder % 1000
    
    if millions > 0:
        million_part = convert_less_than_thousand(millions)
        result.append(f"{million_part} million")
    
    if thousands > 0:
        thousand_part = convert_less_than_thousand(thousands)
        result.append(f"{thousand_part} thousand")
    
    if remainder > 0:
        and_needed = (millions > 0 or thousands > 0) and (remainder < 100)
        remainder_part = convert_less_than_thousand(remainder)
        if and_needed:
            remainder_part = f"and {remainder_part}"
        result.append(remainder_part)
    
    final = ' '.join(result)
    final = final.replace("  ", " ")
    return final.strip()