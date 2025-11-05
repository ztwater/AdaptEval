from funcy import partition

for a, b, c, d in partition(4, ints):
    foo += a * b * c * d
