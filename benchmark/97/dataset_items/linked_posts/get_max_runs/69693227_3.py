import numpy as np


def rle_loop(arr):
    values = []
    lengths = []
    last_x = arr[0]
    length = 1
    for x in arr[1:]:
        if last_x != x:
            values.append(last_x)
            lengths.append(length)
            length = 1
            last_x = x
        else:
            length += 1
    values.append(last_x)
    lengths.append(length)
    return np.array(values), np.array(lengths)
