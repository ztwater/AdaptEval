import itertools
import numpy as np


def rle_groupby(arr):
    values = []
    lengths = []
    for x, group in itertools.groupby(arr):
        values.append(x)
        lengths.append(sum(1 for _ in group))
    return np.array(values), np.array(lengths)
