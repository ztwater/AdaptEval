import numpy as np
from scipy import linalg, sparse

# from .deprecation import deprecated
#
# @deprecated("safe_min is deprecated in version 0.22 and will be removed "
#             "in version 0.24.")
def safe_min(X):
    """Returns the minimum value of a dense or a CSR/CSC matrix.

    Adapated from https://stackoverflow.com/q/13426580

    .. deprecated:: 0.22.0

    Parameters
    ----------
    X : array_like
        The input array or sparse matrix

    Returns
    -------
    Float
        The min value of X
    """
    if sparse.issparse(X):
        if len(X.data) == 0:
            return 0
        m = X.data.min()
        return m if X.getnnz() == X.size else min(m, 0)
    else:
        return X.min()

