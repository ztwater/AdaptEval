from numpy import any, asarray as asa, isnan, NaN, ones, seterr
from numpy.lib.stride_tricks import as_strided as ast
from scipy.stats import nanmean

def _a2t(a):
    """Array to tuple."""
    return tuple(a.tolist())

def _view(D, shape, strides):
    """View of flattened neighbourhood of D."""
    V= ast(D, shape= shape, strides= strides)
    return V.reshape(V.shape[:len(D.shape)]+ (-1,))

def filler(A, n_shape, n_iter= 49):
    """Fill in NaNs from mean calculated from neighbour."""
    # boundary conditions
    D= NaN* ones(_a2t(asa(A.shape)+ asa(n_shape)- 1), dtype= A.dtype)
    slc= tuple([slice(n/ 2, -(n/ 2)) for n in n_shape])
    D[slc]= A

    # neighbourhood
    shape= _a2t(asa(D.shape)- asa(n_shape)+ 1)+ n_shape
    strides= D.strides* 2

    # iterate until no NaNs, but not more than n iterations
    old= seterr(invalid= 'ignore')
    for k in xrange(n_iter):
        M= isnan(D[slc])
        if not any(M): break
        D[slc][M]= nanmean(_view(D, shape, strides), -1)[M]
    seterr(**old)
    A[:]= D[slc]
