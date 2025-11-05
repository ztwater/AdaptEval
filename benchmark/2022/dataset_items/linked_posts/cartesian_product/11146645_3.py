import numpy
import itertools
from functools import reduce

### Two-dimensional products ###

def repeat_product(x, y):
    return numpy.transpose([numpy.tile(x, len(y)), 
                            numpy.repeat(y, len(x))])

def dstack_product(x, y):
    return numpy.dstack(numpy.meshgrid(x, y)).reshape(-1, 2)

### Generalized N-dimensional products ###

def cartesian_product(*arrays):
    la = len(arrays)
    dtype = numpy.result_type(*arrays)
    arr = numpy.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(numpy.ix_(*arrays)):
        arr[...,i] = a
    return arr.reshape(-1, la)

def cartesian_product_transpose(*arrays):
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

# from https://stackoverflow.com/a/1235363/577088

def cartesian_product_recursive(*arrays, out=None):
    arrays = [numpy.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = numpy.prod([x.size for x in arrays])
    if out is None:
        out = numpy.zeros([n, len(arrays)], dtype=dtype)

    m = n // arrays[0].size
    out[:,0] = numpy.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian_product_recursive(arrays[1:], out=out[0:m,1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out

def cartesian_product_itertools(*arrays):
    return numpy.array(list(itertools.product(*arrays)))

### Test code ###

name_func = [('repeat_product',                                                 
              repeat_product),                                                  
             ('dstack_product',                                                 
              dstack_product),                                                  
             ('cartesian_product',                                              
              cartesian_product),                                               
             ('cartesian_product_transpose',                                    
              cartesian_product_transpose),                                     
             ('cartesian_product_recursive',                           
              cartesian_product_recursive),                            
             ('cartesian_product_itertools',                                    
              cartesian_product_itertools)]

def test(in_arrays, test_funcs):
    global func
    global arrays
    arrays = in_arrays
    for name, func in test_funcs:
        print('{}:'.format(name))
        %timeit func(*arrays)

def test_all(*in_arrays):
    test(in_arrays, name_func)

# `cartesian_product_recursive` throws an 
# unexpected error when used on more than
# two input arrays, so for now I've removed
# it from these tests.

def test_cartesian(*in_arrays):
    test(in_arrays, name_func[2:4] + name_func[-1:])

x10 = [numpy.arange(10)]
x50 = [numpy.arange(50)]
x100 = [numpy.arange(100)]
x500 = [numpy.arange(500)]
x1000 = [numpy.arange(1000)]
