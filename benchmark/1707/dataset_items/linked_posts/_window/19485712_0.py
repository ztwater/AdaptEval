def window(seq, size, step=1):
    # initialize iterators
    iters = [iter(seq) for i in range(size)]
    # stagger iterators (without yielding)
    [next(iters[i]) for j in range(size) for i in range(-1, -j-1, -1)]
    while(True):
        yield [next(i) for i in iters]
        # next line does nothing for step = 1 (skips iterations for step > 1)
        [next(i) for i in iters for j in range(step-1)]
