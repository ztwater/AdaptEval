import numpy as np
from skimage.draw import disk
mask = np.zeros((10, 10), dtype=np.uint8)
row = 4
col = 5
radius = 5
# modern scikit uses a tuple for center
rr, cc = disk((row, col), radius)
mask[rr, cc] = 1
