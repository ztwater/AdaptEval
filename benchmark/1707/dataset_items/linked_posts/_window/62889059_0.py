def SlidingWindow(X, window_length, stride):
    indexer = np.arange(window_length)[None, :] + stride*np.arange(int(len(X)/stride)-window_length+4)[:, None]
    return X.take(indexer)
