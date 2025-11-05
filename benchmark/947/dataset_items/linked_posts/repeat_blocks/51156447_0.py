@numba.njit
def repeat_blocks_jit(a, sizes, repeats):
    out = np.empty((sizes * repeats).sum(), a.dtype)
    start = 0
    oi = 0
    for i, size in enumerate(sizes):
        end = start + size
        for rep in range(repeats[i]):
            oe = oi + size
            out[oi:oe] = a[start:end]
            oi = oe
        start = end
    return out
