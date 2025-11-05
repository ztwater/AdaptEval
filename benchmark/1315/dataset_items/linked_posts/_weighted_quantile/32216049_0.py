def weighted_percentile(a, q=np.array([75, 25]), w=None):
    """
    Calculates percentiles associated with a (possibly weighted) array

    Parameters
    ----------
    a : array-like
        The input array from which to calculate percents
    q : array-like
        The percentiles to calculate (0.0 - 100.0)
    w : array-like, optional
        The weights to assign to values of a.  Equal weighting if None
        is specified

    Returns
    -------
    values : np.array
        The values associated with the specified percentiles.  
    """
    # Standardize and sort based on values in a
    q = np.array(q) / 100.0
    if w is None:
        w = np.ones(a.size)
    idx = np.argsort(a)
    a_sort = a[idx]
    w_sort = w[idx]

    # Get the cumulative sum of weights
    ecdf = np.cumsum(w_sort)

    # Find the percentile index positions associated with the percentiles
    p = q * (w.sum() - 1)

    # Find the bounding indices (both low and high)
    idx_low = np.searchsorted(ecdf, p, side='right')
    idx_high = np.searchsorted(ecdf, p + 1, side='right')
    idx_high[idx_high > ecdf.size - 1] = ecdf.size - 1

    # Calculate the weights 
    weights_high = p - np.floor(p)
    weights_low = 1.0 - weights_high

    # Extract the low/high indexes and multiply by the corresponding weights
    x1 = np.take(a_sort, idx_low) * weights_low
    x2 = np.take(a_sort, idx_high) * weights_high

    # Return the average
    return np.add(x1, x2)

# Sample data
a = np.array([1.0, 2.0, 9.0, 3.2, 4.0], dtype=np.float)
w = np.array([2.0, 1.0, 3.0, 4.0, 1.0], dtype=np.float)

# Make an unweighted "copy" of a for testing
a2 = np.repeat(a, w.astype(np.int))

# Tests with different percentiles chosen
q1 = np.linspace(0.0, 100.0, 11)
q2 = np.linspace(5.0, 95.0, 10)
q3 = np.linspace(4.0, 94.0, 10)
for q in (q1, q2, q3):
    assert np.all(weighted_percentile(a, q, w) == np.percentile(a2, q))
