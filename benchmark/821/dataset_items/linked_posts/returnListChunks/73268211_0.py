from math import ceil
import more_itertools as mit
from pprint import pprint

pprint([*mit.chunked_even(range(19), ceil(19 / 5))])
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18]]

pprint([*mit.chunked_even(range(20), ceil(20 / 5))])
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15], [16, 17, 18, 19]]

pprint([*mit.chunked_even(range(21), ceil(21 / 5))])
# [[0, 1, 2, 3, 4],
# [5, 6, 7, 8],
# [9, 10, 11, 12],
# [13, 14, 15, 16],
# [17, 18, 19, 20]]

pprint([*mit.chunked_even(range(3), ceil(3 / 5))])
# [[0], [1], [2]]


