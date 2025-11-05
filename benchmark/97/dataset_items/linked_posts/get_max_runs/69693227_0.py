import numpy as np
import numba as nb


@nb.njit
def count_steps_nb(arr):
    result = 1
    last_x = arr[0]
    for x in arr[1:]:
        if last_x != x:
            result += 1
            last_x = x
    return result


@nb.njit
def rle_nb(arr):
    n = count_steps_nb(arr)
    values = np.empty(n, dtype=arr.dtype)
    lengths = np.empty(n, dtype=np.int_)
    last_x = arr[0]
    length = 1
    i = 0
    for x in arr[1:]:
        if last_x != x:
            values[i] = last_x
            lengths[i] = length
            i += 1
            length = 1
            last_x = x
        else:
            length += 1
    values[i] = last_x
    lengths[i] = length
    return values, lengths
