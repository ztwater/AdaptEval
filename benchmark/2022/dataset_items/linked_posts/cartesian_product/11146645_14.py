>>> x, y = numpy.arange(1000), numpy.arange(1000)
>>> %timeit cartesian([x, y])
10 loops, best of 3: 25.4 ms per loop
>>> %timeit dstack_product(x, y)
10 loops, best of 3: 66.6 ms per loop
