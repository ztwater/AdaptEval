quantiles, idx = np.unique(sample, return_inverse=True)
counts = np.bincount(idx)
