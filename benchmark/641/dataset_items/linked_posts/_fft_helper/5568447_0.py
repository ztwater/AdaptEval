import numpy
a = numpy.array([1, 2, 3, 4])
b = numpy.ones((1000, a.shape[0]))
b *= a
b = b.flatten()
