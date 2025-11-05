import numpy as np

def cartesian_product(*args: np.ndarray) -> np.ndarray:
    """
    Produce the cartesian product of arbitrary length vectors.

    Parameters
    ----------
    np.ndarray args
        vector of points of interest in each dimension

    Returns
    -------
    np.ndarray
        the cartesian product of size [m x n] wherein:
            m = prod([len(a) for a in args])
            n = len(args)
    """
    for i, a in enumerate(args):
        assert a.ndim == 1, "arg {:d} is not rank 1".format(i)
    return np.concatenate([np.reshape(xi, [-1, 1]) for xi in np.meshgrid(*args)], axis=1)
