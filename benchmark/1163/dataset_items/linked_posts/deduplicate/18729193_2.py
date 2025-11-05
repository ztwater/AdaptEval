In [122]: %timeit unique(np.random.randint(5, size=(1)))
10000 loops, best of 3: 25.3 us per loop

In [123]: %timeit unique(np.random.randint(5, size=(10)))
10000 loops, best of 3: 42.9 us per loop

In [124]: %timeit unique(np.random.randint(5, size=(100)))
10000 loops, best of 3: 132 us per loop

In [125]: %timeit unique(np.random.randint(5, size=(1000)))
1000 loops, best of 3: 1.05 ms per loop

In [126]: %timeit unique(np.random.randint(5, size=(10000)))
100 loops, best of 3: 11 ms per loop
