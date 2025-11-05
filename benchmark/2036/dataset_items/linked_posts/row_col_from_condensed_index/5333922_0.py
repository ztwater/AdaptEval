import numpy as np

def f(c,n):
    tt = np.zeros_like(c)
    tt[n] = 1
    return tuple(np.nonzero(squareform(tt))[0])
