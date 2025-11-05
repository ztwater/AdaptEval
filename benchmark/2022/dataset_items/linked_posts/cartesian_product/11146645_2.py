def cartesian_product_simple_transpose(arrays):
    la = len(arrays)
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty([la] + [len(a) for a in arrays], dtype=dtype)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[i, ...] = a
    return arr.reshape(la, -1).T
