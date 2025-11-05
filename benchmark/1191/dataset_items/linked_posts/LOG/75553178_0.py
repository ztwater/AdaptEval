import numpy as np
arr = np.array([74088, 3111696])      # = [42^3, 42^4]
base = 42
np.emath.logn(base, arr)              # array([3., 4.])

np.emath.logn(14, 14**3)              # 3.0
