import tensorflow as tf

def cartesian_product(*args: tf.Tensor) -> tf.Tensor:
    """
    Produce the cartesian product of arbitrary length vectors.

    Parameters
    ----------
    tf.Tensor args
        vector of points of interest in each dimension

    Returns
    -------
    tf.Tensor
        the cartesian product of size [m x n] wherein:
            m = prod([len(a) for a in args])
            n = len(args)
    """
    for i, a in enumerate(args):
        tf.assert_rank(a, 1, message="arg {:d} is not rank 1".format(i))
    return tf.concat([tf.reshape(xi, [-1, 1]) for xi in tf.meshgrid(*args)], axis=1)
