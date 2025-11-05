import numpy as np
def angle(vec_0, vec_1, axis):
    return np.arctan2(np.cross(vec_0, vec_1, axis = axis), np.sum(vec_0*vec_1, axis = axis))
