from itertools import product
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5])
cart_prod = np.array(list(product(*[x, y])),dtype='int32')
