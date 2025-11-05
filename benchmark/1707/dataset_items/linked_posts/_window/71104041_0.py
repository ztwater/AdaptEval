>>> from cytoolz import sliding_window
>>> list(sliding_window(3, range(6))) # returns [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
