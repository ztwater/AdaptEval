from itertools import islice
array = range(0, 10)
window_size = 4
map(lambda i: list(islice(array, i, i + window_size)), range(0, len(array) - window_size + 1))
# output = [[0, 1, 2, 3], [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8], [6, 7, 8, 9]]
