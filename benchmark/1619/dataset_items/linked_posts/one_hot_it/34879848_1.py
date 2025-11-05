In [62]: c = np.array([[1,0,0],[1,0,0],[1,0,0],[1,1,0]])

In [63]: c
Out[63]: 
array([[1, 0, 0],
       [1, 0, 0],
       [1, 0, 0],
       [1, 1, 0]])

In [64]: np.bitwise_and.reduce(c) == c[0]
Out[64]: array([ True,  True,  True], dtype=bool)
