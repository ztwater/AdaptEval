xx = np.random.randint(0, 2, 20)

xx
Out[60]: array([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1])

am = runs_of_ones_array(xx)

tb = rle(xx)

am
Out[63]: array([4, 5, 2, 5])

tb[0][tb[2] == 1]
Out[64]: array([4, 5, 2, 5])

%timeit runs_of_ones_array(xx)
10000 loops, best of 3: 28.5 µs per loop

%timeit rle(xx)
10000 loops, best of 3: 38.2 µs per loop
