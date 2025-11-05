In []: x= ones((3, 6, 99))
In []: x.sum(-1)
Out[]:
array([[ 99.,  99.,  99.,  99.,  99.,  99.],
       [ 99.,  99.,  99.,  99.,  99.,  99.],
       [ 99.,  99.,  99.,  99.,  99.,  99.]])
In []: x= NaN* x
In []: x[1, 2, 3]= 1
In []: x.sum(-1)
Out[]:
array([[ nan,  nan,  nan,  nan,  nan,  nan],
       [ nan,  nan,  nan,  nan,  nan,  nan],
       [ nan,  nan,  nan,  nan,  nan,  nan]])
In []: filler(x, (3, 3, 5))
In []: x.sum(-1)
Out[]:
array([[ 99.,  99.,  99.,  99.,  99.,  99.],
       [ 99.,  99.,  99.,  99.,  99.,  99.],
       [ 99.,  99.,  99.,  99.,  99.,  99.]])
