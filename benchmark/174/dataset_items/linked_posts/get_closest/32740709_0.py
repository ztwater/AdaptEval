In [1]: from scipy import spatial

In [2]: import numpy as np

In [3]: A = np.random.random((10,2))*100

In [4]: A
Out[4]:
array([[ 68.83402637,  38.07632221],
       [ 76.84704074,  24.9395109 ],
       [ 16.26715795,  98.52763827],
       [ 70.99411985,  67.31740151],
       [ 71.72452181,  24.13516764],
       [ 17.22707611,  20.65425362],
       [ 43.85122458,  21.50624882],
       [ 76.71987125,  44.95031274],
       [ 63.77341073,  78.87417774],
       [  8.45828909,  30.18426696]])

In [5]: pt = [6, 30]  # <-- the point to find

In [6]: A[spatial.KDTree(A).query(pt)[1]] # <-- the nearest point 
Out[6]: array([  8.45828909,  30.18426696])

#how it works!
In [7]: distance,index = spatial.KDTree(A).query(pt)

In [8]: distance # <-- The distances to the nearest neighbors
Out[8]: 2.4651855048258393

In [9]: index # <-- The locations of the neighbors
Out[9]: 9

#then 
In [10]: A[index]
Out[10]: array([  8.45828909,  30.18426696])
