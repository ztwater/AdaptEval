In [115]: %timeit original(prob_matrix, items)
1 loops, best of 3: 270 ms per loop

In [116]: %timeit improved(prob_matrix, items)
10 loops, best of 3: 24.9 ms per loop

In [117]: %timeit vectorized(prob_matrix, items)
1000 loops, best of 3: 1 ms per loop
