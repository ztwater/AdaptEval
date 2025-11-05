>>> %timeit -r5 deque(windowkindall(range(10), 3), 0)
100000 loops, best of 5: 1.87 μs per loop
>>> %timeit -r5 deque(windowkindall(range(1000), 3), 0)
10000 loops, best of 5: 72.6 μs per loop
>>> %timeit -r5 deque(windowkindall(range(1000), 30), 0)
1000 loops, best of 5: 71.6 μs per loop
