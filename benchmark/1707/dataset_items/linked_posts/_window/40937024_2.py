>>> %timeit -r5 deque(windowkindalltupled(range(10), 3), 0)
100000 loops, best of 5: 3.05 μs per loop
>>> %timeit -r5 deque(windowkindalltupled(range(1000), 3), 0)
10000 loops, best of 5: 207 μs per loop
>>> %timeit -r5 deque(windowkindalltupled(range(1000), 30), 0)
1000 loops, best of 5: 348 μs per loop
