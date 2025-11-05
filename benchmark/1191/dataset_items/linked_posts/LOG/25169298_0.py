import numpy as np
array = np.array([74088, 3111696])  # = [42^3, 42^4]
base = 42
exponent = np.emath.logn(base, array)  # = [3, 4]
