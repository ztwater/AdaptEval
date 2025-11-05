from functools import reduce
import itertools
import numpy
import perfplot


def dstack_product(arrays):
    return numpy.dstack(numpy.meshgrid(*arrays, indexing="ij")).reshape(-1, len(arrays))


# Generalized N-dimensional products
def cartesian_product(arrays):
    la = len(arrays)
    dtype = numpy.find_common_type([a.dtype for a in arrays], [])
    arr = numpy.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[..., i] = a
    return arr.reshape(-1, la)


def cartesian_product_transpose(arrays):
    broadcastable = numpy.ix_(*arrays)
    broadcasted = numpy.broadcast_arrays(*broadcastable)
    rows, cols = reduce(numpy.multiply, broadcasted[0].shape), len(broadcasted)
    dtype = numpy.find_common_type([a.dtype for a in arrays], [])

    out = numpy.empty(rows * cols, dtype=dtype)
    start, end = 0, rows
    for a in broadcasted:
        out[start:end] = a.reshape(-1)
        start, end = end, end + rows
    return out.reshape(cols, rows).T


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
            out[j * m : (j + 1) * m, 1:] = out[0:m, 1:]
    return out


def cartesian_product_itertools(arrays):
    return numpy.array(list(itertools.product(*arrays)))


perfplot.show(
    setup=lambda n: 2 * (numpy.arange(n, dtype=float),),
    n_range=[2 ** k for k in range(13)],
    # setup=lambda n: 4 * (numpy.arange(n, dtype=float),),
    # n_range=[2 ** k for k in range(6)],
    kernels=[
        dstack_product,
        cartesian_product,
        cartesian_product_transpose,
        cartesian_product_recursive,
        cartesian_product_itertools,
    ],
    logx=True,
    logy=True,
    xlabel="len(a), len(b)",
    equality_check=None,
)
