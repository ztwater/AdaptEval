>>> a = np.array([[[1.0,1.0,0.9],
...                [1.0,1.1,1.1]],
...               [[1.0,1.0,1.0],
...                [0.99999,1.0,1.09999]]])
>>> isconst(a, axis=0)
array([[ True,  True, False],
       [ True, False,  True]])
>>> isconst(a, axis=0, rtol=1.0e-8)
array([[ True,  True, False],
       [False, False, False]])
