import numpy as np
from tifffile import imsave

# Generate float data
b=np.random.random_sample((768,1024,3)).astype(np.float32)

# Save as TIF - when reading, use "data = imread('file.tif')"
imsave('result.tif',b)
