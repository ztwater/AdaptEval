at = np.tile(np.reshape(a, (-1, *list(np.ones(len(b.shape)).astype(int)))), (1, *b.shape))
bt = np.tile(b, (a.size, *list(np.ones(len(b.shape)).astype(int))))
