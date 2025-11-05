import numpy as np

def unstack(a, axis = 0):
    return [np.squeeze(e, axis) for e in np.split(a, a.shape[axis], axis = axis)]

a = [np.array([[1,2,3],[4,5,6]]), np.array([[7,8,9],[10,11,12]])]

for axis in range(len(a[0].shape) + 1):
    b = np.stack(a, axis)
    c = unstack(b, axis)
    # Check that we have same "c" as input "a"
    assert len(c) == len(a) and all(np.all(sc == sa) for sc, sa in zip(c, a)), (c, a)
