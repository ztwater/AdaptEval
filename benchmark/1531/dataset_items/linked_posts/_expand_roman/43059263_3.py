from itertools import tee

def parse_roman(s):
    numerals = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    cur, prev = tee(numerals[c] for c in reversed(s.upper()))
    return next(cur) + sum((cur, -cur)[cur < prev] for cur, prev in zip(cur,prev))
