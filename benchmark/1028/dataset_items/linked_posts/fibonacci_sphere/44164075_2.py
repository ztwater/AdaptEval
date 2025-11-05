def continued_fraction(r):
    while r != 0:
        n = floor(r)
        yield n
        r = 1/(r - n)
