from cmath import inf

import numba
import numpy as np


@numba.njit
def get_indices_of_closest_questioned_points(
    interogators: npt.NDArray,
    questioned: npt.NDArray,
) -> npt.NDArray:
    """For each element in `interogators` get the index of the closest element in set `questioned`.
    """
    res = np.empty(shape=interogators.shape, dtype=np.uint32)
    N = len(interogators)
    M = len(questioned)
    n = m = 0
    closest_left_to_x = -inf
    while n < N and m < M:
        x = interogators[n]
        y = questioned[m]
        if y < x:
            closest_left_to_x = y
            m += 1
        else:
            res[n] = m - (x - closest_left_to_x < y - x)
            n += 1
    while n < N:
        res[n] = M - 1
        n += 1
    return res
