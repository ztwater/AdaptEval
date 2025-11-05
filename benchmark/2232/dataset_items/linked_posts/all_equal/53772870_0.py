import numpy as np
def allthesame(l):
    return np.all(np.diff(l)==0)
