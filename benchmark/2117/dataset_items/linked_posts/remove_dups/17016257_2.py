>>> from more_itertools import unique_everseen
>>> items = [1, 2, 0, 1, 3, 2]
>>> list(unique_everseen(items))
[1, 2, 0, 3]
