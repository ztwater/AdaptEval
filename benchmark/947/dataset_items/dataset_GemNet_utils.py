import numpy as np


def repeat_blocks(sizes, repeats):
    """Repeat blocks of indices.
    From https://stackoverflow.com/questions/51154989/numpy-vectorized-function-to-repeat-blocks-of-consecutive-elements
    Examples
    --------
        sizes = [1,3,2] ; repeats = [3,2,3]
        Return: [0 0 0  1 2 3 1 2 3  4 5 4 5 4 5]
        sizes = [0,3,2] ; repeats = [3,2,3]
        Return: [0 1 2 0 1 2  3 4 3 4 3 4]
        sizes = [2,3,2] ; repeats = [2,0,2]
        Return: [0 1 0 1  5 6 5 6]
    """
    a = np.arange(np.sum(sizes))
    indices = np.empty((sizes * repeats).sum(), dtype=np.int32)
    start = 0
    oi = 0
    for i, size in enumerate(sizes):
        end = start + size
        for _ in range(repeats[i]):
            oe = oi + size
            indices[oi:oe] = a[start:end]
            oi = oe
        start = end
    return indices
