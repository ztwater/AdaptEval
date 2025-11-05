size = 1000
n = 3 # or any positive integer
x = numpy.random.normal(size=(size, n)) 
x /= numpy.linalg.norm(x, axis=1)[:, numpy.newaxis]
