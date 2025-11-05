# Provides parsing of numbers to text
"""
This module provides parsing of numeric types in English to text.
Modified from https://github.com/keithito/tacotron
""" 
 
def _expand_roman(m):
    # from https://stackoverflow.com/questions/19308177/converting-roman-numerals-to-integers-in-python
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    num = m.group(0)
    for i, c in enumerate(num):
        if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
            result += roman_numerals[c]
        else:
            result -= roman_numerals[c]
    return str(result) 