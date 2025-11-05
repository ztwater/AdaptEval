import numpy
import numpy as np
from functools import reduce
import itertools
import timeit
import perfplot

def dstack_product(arrays):
    return numpy.dstack(
        numpy.meshgrid(*arrays, indexing='ij')
        ).reshape(-1, len(arrays))

def cartesian_product_transpose_pp(arrays):
    la = len(arrays)
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty((la, *map(len, arrays)), dtype=dtype)
    idx = slice(None), *itertools.repeat(None, la)
    for i, a in enumerate(arrays):
        arr[i, ...] = a[idx[:la-i]]
    return arr.reshape(la, -1).T

def cartesian_product(arrays):
    la = len(arrays)
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

def cartesian_product_transpose(arrays):
    broadcastable = numpy.ix_(*arrays)
    broadcasted = numpy.broadcast_arrays(*broadcastable)
    rows, cols = numpy.prod(broadcasted[0].shape), len(broadcasted)
    dtype = numpy.result_type(*arrays)

    out = numpy.empty(rows * cols, dtype=dtype)
    start, end = 0, rows
    for a in broadcasted:
        out[start:end] = a.reshape(-1)
        start, end = end, end + rows
    return out.reshape(cols, rows).T

from itertools import accumulate, repeat, chain

def cartesian_product_pp(arrays, out=None):
    la = len(arrays)
    L = *map(len, arrays), la
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty(L, dtype=dtype)
    arrs = *accumulate(chain((arr,), repeat(0, la-1)), np.ndarray.__getitem__),
    idx = slice(None), *itertools.repeat(None, la-1)
    for i in range(la-1, 0, -1):
        arrs[i][..., i] = arrays[i][idx[:la-i]]
        arrs[i-1][1:] = arrs[i]
    arr[..., 0] = arrays[0][idx]
    return arr.reshape(-1, la)

def cartesian_product_itertools(arrays):
    return numpy.array(list(itertools.product(*arrays)))


# from https://stackoverflow.com/a/1235363/577088
def cartesian_product_recursive(arrays, out=None):
    arrays = [numpy.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = numpy.prod([x.size for x in arrays])
    if out is None:
        out = numpy.zeros([n, len(arrays)], dtype=dtype)

    m = n // arrays[0].size
    out[:, 0] = numpy.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian_product_recursive(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]
    return out

### Test code ###
if False:
  perfplot.save('cp_4el_high.png',
    setup=lambda n: n*(numpy.arange(4, dtype=float),),
                n_range=list(range(6, 11)),
    kernels=[
        dstack_product,
        cartesian_product_recursive,
        cartesian_product,
#        cartesian_product_transpose,
        cartesian_product_pp,
#        cartesian_product_transpose_pp,
        ],
    logx=False,
    logy=True,
    xlabel='#factors',
    equality_check=None
    )
else:
  perfplot.save('cp_2f_T.png',
    setup=lambda n: 2*(numpy.arange(n, dtype=float),),
    n_range=[2**k for k in range(5, 11)],
    kernels=[
#        dstack_product,
#        cartesian_product_recursive,
#        cartesian_product,
        cartesian_product_transpose,
#        cartesian_product_pp,
        cartesian_product_transpose_pp,
        ],
    logx=True,
    logy=True,
    xlabel='length of each factor',
    equality_check=None
    )
