from functors import reduce
from operator import mul

def cartesian_product(arrays):
    return np.vstack(
        np.tile(
            np.repeat(arrays[j], reduce(mul, map(len, arrays[j+1:]), 1)),
            reduce(mul, map(len, arrays[:j]), 1),
        )
        for j in range(len(arrays))
    ).T
