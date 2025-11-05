import numpy as np
from scipy.spatial import distance

test = np.random.rand(1000,1000)
condense = distance.pdist(test)
sample = np.random.randint(0,len(condense), 1000)

%timeit res = vec_row_col(1000, sample)
10000 loops, best of 3: 156 µs per loop

res = []
%timeit for i in sample: res.append(row_col_from_condensed_index(1000, i))
100 loops, best of 3: 5.87 ms per loop
