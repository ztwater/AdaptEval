import numpy as np
def SlidingWindow(X, window_length, stride1):
    stride=  X.shape[1]*stride1
    window_length = window_length*X.shape[1]
    indexer = np.arange(window_length)[None, :] + stride1*np.arange(int(len(X)/stride1)-window_length-1)[:, None]
    return X.take(indexer)
