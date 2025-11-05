import numpy as np

def find_nearest(array, values):
    indices = np.abs(np.subtract.outer(array, values)).argmin(0)
    return array[indices]
