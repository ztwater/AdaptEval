import numpy as np
def find_nearest(array, value, k):
    array = np.asarray(array)
    idx = np.argsort(abs(array - value))[:k]
    return array[idx]
