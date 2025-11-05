# np.squeeze
❯ python -m timeit -s "import numpy as np; a=np.array(np.meshgrid(np.arange(1000), np.arange(1000)));" "C = [np.squeeze(e, 1) for e in np.split(a, a.shape[1], axis = 1)]"
100 loops, best of 5: 2.64 msec per loop
    
# np.take
❯ python -m timeit -s "import numpy as np; a=np.array(np.meshgrid(np.arange(1000), np.arange(1000)));" "C = [np.take(a, i, axis = 1) for i in range(a.shape[1])]"       
50 loops, best of 5: 5.08 msec per loop

# np.moveaxis
❯ python -m timeit -s "import numpy as np; a=np.array(np.meshgrid(np.arange(1000), np.arange(1000)));" "C = np.moveaxis(a, 1, 0)"
100000 loops, best of 5: 3.89 usec per loop

# list(np.moveaxis)
❯ python -m timeit -s "import numpy as np; a=np.array(np.meshgrid(np.arange(1000), np.arange(1000)));" "C = list(np.moveaxis(a, 1, 0))"
1000 loops, best of 5: 205 usec per loop
