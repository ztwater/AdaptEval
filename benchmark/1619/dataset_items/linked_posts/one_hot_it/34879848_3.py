In [69]: np.logical_and(np.bitwise_or.reduce(a) == a[0], np.bitwise_and.reduce(a) == a[0])
Out[69]: array([ True, False,  True], dtype=bool)

In [70]: np.logical_and(np.bitwise_or.reduce(b) == b[0], np.bitwise_and.reduce(b) == b[0])
Out[70]: array([ True, False,  True], dtype=boo

In [71]: np.logical_and(np.bitwise_or.reduce(c) == c[0], np.bitwise_and.reduce(c) == c[0])
Out[71]: array([ True, False,  True], dtype=bool)
