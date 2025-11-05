def find_nearest(X, value):
    return X[np.unravel_index(np.argmin(np.abs(X - value)), X.shape)]
