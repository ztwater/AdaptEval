xx = np.random.randint(0, 5, 1000000)
%timeit yy = rle(xx)
100 loops, best of 3: 18.6 ms per loop
