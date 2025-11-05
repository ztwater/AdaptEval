>>> x, y = numpy.arange(500), numpy.arange(500)
>>> %timeit repeat_product(x, y)
10 loops, best of 3: 62 ms per loop
>>> %timeit dstack_product(x, y)
100 loops, best of 3: 12.2 ms per loop
