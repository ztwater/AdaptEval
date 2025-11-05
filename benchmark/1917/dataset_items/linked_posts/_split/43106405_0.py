>>> import numpy as np
>>> print(*np.array_split(range(10), 3))
[0 1 2 3] [4 5 6] [7 8 9]
>>> print(*np.array_split(range(10), 4))
[0 1 2] [3 4 5] [6 7] [8 9]
>>> print(*np.array_split(range(10), 5))
[0 1] [2 3] [4 5] [6 7] [8 9]
