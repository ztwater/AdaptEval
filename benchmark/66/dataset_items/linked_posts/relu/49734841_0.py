import numpy as np

def baseline():
    x = np.random.random((5000, 5000)) - 0.5
    return x

def relu_mul():
    x = np.random.random((5000, 5000)) - 0.5
    out = x * (x > 0)
    return out

def relu_max():
    x = np.random.random((5000, 5000)) - 0.5
    out = np.maximum(x, 0)
    return out

def relu_max_inplace():
    x = np.random.random((5000, 5000)) - 0.5
    np.maximum(x, 0, x)
    return x 
