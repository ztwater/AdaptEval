def find_nearest(array, values):
    values = np.atleast_1d(values)
    indices = np.abs(np.subtract.outer(array, values)).argmin(0)
    out = array[indices]
    return out if len(out) > 1 else out[0]
