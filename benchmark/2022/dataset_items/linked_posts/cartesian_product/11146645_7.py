In [1]: import numpy
In [2]: x = numpy.array([1,2,3])
   ...: y = numpy.array([4,5])
   ...: 

In [3]: [numpy.tile(x, len(y)), numpy.repeat(y, len(x))]
Out[3]: [array([1, 2, 3, 1, 2, 3]), array([4, 4, 4, 5, 5, 5])]
