def round_to_nearest_in(a, b):
    n = len(b)
    shp = list(a.shape) + [n]

    broad = np.repeat(a, n).reshape((shp))
    diffs = np.abs(broad - b)

    return b[diffs.argmin(-1)]
