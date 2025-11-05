from itertools import *

class SENTINEL: pass

def batch(iterable, n):
    return (tuple(filterfalse(lambda x: x is SENTINEL, group)) for group in zip_longest(fillvalue=SENTINEL, *[iter(iterable)] * n))

print(list(range(10), 3)))
# outputs: [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9,)]
print(list(batch([None]*10, 3)))
# outputs: [(None, None, None), (None, None, None), (None, None, None), (None,)]
