import more_itertools as mit


list(mit.chunked(range(9), 5))
# [[0, 1, 2, 3, 4], [5, 6, 7, 8]]
