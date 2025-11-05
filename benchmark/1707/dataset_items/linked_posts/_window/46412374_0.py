import more_itertools
list(more_itertools.windowed([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],n=3, step=3))

Out: [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15)]
