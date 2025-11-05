mapping = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M':1000}

def roman_to_dec(roman):
"""
Convert the roman no to decimal
"""
dec = last = 0
for i in range(0, len(roman)):
    no = mapping.get(roman[i])
    # subtract last 2 times cuz one for this pass and another for last pass
    dec = dec + (no - 2 * last) if no > last else dec + no
    last = no
return dec
