def np_z_trim(x, threshold=10, axis=0):
    """ Replace outliers in numpy ndarray along axis with min or max values
    within the threshold along this axis, whichever is closer."""
    mean = np.mean(x, axis=axis, keepdims=True)
    std = np.std(x, axis=axis, keepdims=True)
    masked = np.where(np.abs(x - mean) < threshold * std, x, np.nan)
    min = np.nanmin(masked, axis=axis, keepdims=True)
    max = np.nanmax(masked, axis=axis, keepdims=True)
    repl = np.where(np.abs(x - max) < np.abs(x - min), max, min)
    return np.where(np.isnan(masked), repl, masked)
