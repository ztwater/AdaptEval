>>> %timeit ar=get_closest(np.linspace(1, 1000, 100), np.random.randint(0, 1050, (1000, 1000)))
139 ms ± 4.04 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

>>> %timeit ar=[find_nearest(np.linspace(1, 1000, 100), value) for value in np.random.randint(0, 1050, 1000*1000)]
took 21.4 seconds
