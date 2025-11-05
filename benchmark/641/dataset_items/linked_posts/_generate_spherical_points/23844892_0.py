N = 1000
v = numpy.random.uniform(size=(3,N)) 
vn = v / numpy.sqrt(numpy.sum(v**2, 0))
