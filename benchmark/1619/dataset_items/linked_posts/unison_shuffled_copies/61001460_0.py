import numpy as np

def shuffle_2d(a, b):
    rows= a.shape[0]
    if b.shape != (rows,1):
        b = b.reshape((rows,1))
    S = np.hstack((b,a))
    np.random.shuffle(S)
    b, a  = S[:,0], S[:,1:]
    return a,b

features, samples = 2, 5
x, y = np.random.random((samples, features)), np.arange(samples)
x, y = shuffle_2d(train, test)
