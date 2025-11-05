from itertools import islice
from functools import partial

seq = [1,2,3,4,5,6,7]
size = 3
result = list(iter(partial(lambda it: tuple(islice(it, size)), iter(seq)), ()))
assert result == [(1, 2, 3), (4, 5, 6), (7,)]
