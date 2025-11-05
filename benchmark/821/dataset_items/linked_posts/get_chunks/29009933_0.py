from itertools import zip_longest

a = range(1, 16)
i = iter(a)
r = list(zip_longest(i, i, i))
>>> print(r)
[(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]
