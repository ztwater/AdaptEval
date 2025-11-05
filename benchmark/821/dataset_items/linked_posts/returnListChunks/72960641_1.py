from itertools import batched
list(batched(range(7), 3))  # [(0, 1, 2), (3, 4, 5), (6,)]
