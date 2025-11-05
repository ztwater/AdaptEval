#Importing the numpy library
import numpy as np
arr = np.arange(6) #Sequence
window_size = 3
np.lib.stride_tricks.as_strided(arr, shape= (len(arr) - window_size +1, window_size), 
strides = arr.strides*2)

"""Example output:

  [0, 1, 2]
  [1, 2, 3]
  [2, 3, 4]
  [3, 4, 5]
