data = [[1, 2, 3],
[4, 5],
[6, 8, 9, 10],
[11]]
from itertools import zip_longest
[i for lst in zip_longest(*data) for i in lst if i is not None]
