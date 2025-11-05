list(mit.chunked(iterable, n))
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10]]

list(mit.sliced(iterable, n))
# [range(0, 3), range(3, 6), range(6, 9), range(9, 11)]

list(mit.grouper(n, iterable))
# [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, None)]

list(mit.windowed(iterable, len(iterable)//n, step=n))
# [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, None)]

list(mit.chunked_even(iterable, n))
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10]]
