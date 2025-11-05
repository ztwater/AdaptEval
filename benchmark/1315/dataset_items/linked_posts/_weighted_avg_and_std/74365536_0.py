def std(values, weights=None, axis=None):
    """
    Return the weighted standard deviation.
    axis -- the axis for std calculation
    values, weights -- Numpy ndarrays with the same shape on the according axis.
    """
    average = np.expand_dims(np.average(values, weights=weights, axis=axis), axis=axis)
    # Fast and numerically precise:
    variance = np.average((values-average)**2, weights=weights, axis=axis)
    return np.sqrt(variance)
