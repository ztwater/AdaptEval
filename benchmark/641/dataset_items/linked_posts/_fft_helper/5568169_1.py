b = np.lib.stride_tricks.as_strided(a, (1000, a.size), (0, a.itemsize))
