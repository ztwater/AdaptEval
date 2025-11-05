import numpy
def join_2d(a, b):
    assert a.dtype == b.dtype
    a_part = numpy.tile(a, (len(b), 1))
    b_part = numpy.repeat(b, len(a), axis=0)
    return numpy.hstack((a_part, b_part))
