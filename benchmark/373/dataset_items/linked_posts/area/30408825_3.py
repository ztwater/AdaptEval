%timeit PolyArea(x,y)
# 10000 loops, best of 3: 42 µs per loop
%timeit PolygonArea(zip(x,y))
# 100 loops, best of 3: 2.09 ms per loop.
