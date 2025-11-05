import numpy as np
def find_nearest(a, a0):
    idx = (np.abs(a - a0)).argmin()
    w = a.shape[1]
    i = idx // w
    j = idx - i * w
    return a[i,j], i, j
