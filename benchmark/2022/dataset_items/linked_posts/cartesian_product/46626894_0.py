import numpy as np

def cartesian_product(*arrays):
    ndim = len(arrays)
    return (np.stack(np.meshgrid(*arrays), axis=-1)
              .reshape(-1, ndim))

a = np.array([1,2])
b = np.array([10,20])
cartesian_product(a,b)

# output:
# array([[ 1, 10],
#        [ 2, 10],
#        [ 1, 20],
#        [ 2, 20]])  
