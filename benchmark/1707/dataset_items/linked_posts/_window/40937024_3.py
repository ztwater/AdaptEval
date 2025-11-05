>>> %timeit -r5 deque(windowconsume(range(10), 3), 0)
100000 loops, best of 5: 3.92 μs per loop
>>> %timeit -r5 deque(windowconsume(range(1000), 3), 0)
10000 loops, best of 5: 42.8 μs per loop
>>> %timeit -r5 deque(windowconsume(range(1000), 30), 0)
1000 loops, best of 5: 232 μs per loop
