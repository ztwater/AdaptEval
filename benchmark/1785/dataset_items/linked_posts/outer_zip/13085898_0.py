>>> from itertools import zip_longest
>>> a = [1,2,3]
>>> b = [4,5,6,7]
>>> list(zip_longest(a, b, fillvalue=0))
[(1, 4), (2, 5), (3, 6), (0, 7)]
