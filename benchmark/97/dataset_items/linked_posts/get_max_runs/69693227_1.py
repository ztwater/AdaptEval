import numpy as np


def rle_np_neq(arr):
    n = len(arr)
    if n == 0:
        values = np.empty(0, dtype=arr.dtype)
        lengths = np.empty(0, dtype=np.int_)
    else:
        positions = np.concatenate(
            [[-1], np.nonzero(arr[1:] != arr[:-1])[0], [n - 1]])
        lengths = positions[1:] - positions[:-1]
        values = arr[positions[1:]]
    return values, lengths
