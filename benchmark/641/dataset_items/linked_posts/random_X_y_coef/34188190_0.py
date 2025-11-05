def improved(prob_matrix, items):
    # transpose here for better data locality later
    cdf = np.cumsum(prob_matrix.T, axis=1)
    # random numbers are expensive, so we'll get all of them at once
    ridx = np.random.random(size=n)
    # the one loop we can't avoid, made as simple as possible
    idx = np.zeros(n, dtype=int)
    for i, r in enumerate(ridx):
      idx[i] = np.searchsorted(cdf[i], r)
    # fancy indexing all at once is faster than indexing in a loop
    return items[idx]
