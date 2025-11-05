setup = 'import copy; l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]'
timeit.timeit(setup = setup, stmt='m=l[:]')
timeit.timeit(setup = setup, stmt='m=l.copy()')
timeit.timeit(setup = setup, stmt='m=copy.deepcopy(l)')
