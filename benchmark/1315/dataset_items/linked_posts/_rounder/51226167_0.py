import numpy as np

def rounder(values):
    def f(x):
        idx = np.argmin(np.abs(values - x))
        return values[idx]
    return np.frompyfunc(f, 1, 1)

a = np.random.normal(size=(5,))
b = np.random.normal(size=(10,10))
rounded = rounder(a)(b)
print(rounded)
