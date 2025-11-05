import numpy as np
from bisect import bisect


a = np.random.normal(size=(5,))

b = np.random.normal(size=(10, 10))
a.sort()
size = a.size


for sub in b:
    for ind2, ele in enumerate(sub):
        i = bisect(a, ele, hi=size-1)
        i1, i2 = a[i], a[i-1]
        sub[ind2] = i1 if abs(i1 - ele) < abs(i2 - ele) else i2
