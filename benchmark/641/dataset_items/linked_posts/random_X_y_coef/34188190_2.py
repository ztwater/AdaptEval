In [45]: %timeit original(prob_matrix, items)
100 loops, best of 3: 2.86 ms per loop

In [46]: %timeit improved(prob_matrix, items)
The slowest run took 4.15 times longer than the fastest. This could mean that an intermediate result is being cached
10000 loops, best of 3: 157 µs per loop
