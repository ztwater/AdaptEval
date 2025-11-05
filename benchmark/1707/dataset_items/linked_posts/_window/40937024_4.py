>>> %timeit -r5 deque(windowinlineconsume(range(10), 3), 0)
100000 loops, best of 5: 3.57 μs per loop
>>> %timeit -r5 deque(windowinlineconsume(range(1000), 3), 0)
10000 loops, best of 5: 40.9 μs per loop
>>> %timeit -r5 deque(windowinlineconsume(range(1000), 30), 0)
1000 loops, best of 5: 211 μs per loop
