import numpy as np
arr = np.arange(10)
repeated = np.broadcast_to(arr, (1000, arr.size))
