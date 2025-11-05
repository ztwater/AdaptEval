import numpy as np
def allthesame(l):
    return np.unique(l).shape[0]<=1
