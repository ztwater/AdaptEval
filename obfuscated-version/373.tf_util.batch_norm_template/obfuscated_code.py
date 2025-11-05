import numpy as np
import tensorflow as tf
from tensorflow.python import control_flow_ops

def batch_norm(var_0, var_1, var_2, var_3='bn'):
    """
    Batch normalization on convolutional maps.
    Args:
        x:           Tensor, 4D BHWD input maps
        n_out:       integer, depth of input maps
        phase_train: boolean tf.Varialbe, true indicates training phase
        scope:       string, variable scope
    Return:
        normed:      batch-normalized maps
    """
    with tf.variable_scope(var_3):
        var_4 = tf.Variable(tf.constant(0.0, shape=[var_1]),
                                     name='beta', trainable=True)
        var_5 = tf.Variable(tf.constant(1.0, shape=[var_1]),
                                      name='gamma', trainable=True)
        batch_mean, batch_var = tf.nn.moments(var_0, [0,1,2], name='moments')
        var_6 = tf.train.ExponentialMovingAverage(decay=0.5)

        def mean_var_with_update():
            var_7 = var_6.apply([batch_mean, batch_var])
            with tf.control_dependencies([var_7]):
                return tf.identity(batch_mean), tf.identity(batch_var)

        mean, var = tf.cond(var_2,
                            mean_var_with_update,
                            lambda: (var_6.average(batch_mean), var_6.average(batch_var)))
        var_8 = tf.nn.batch_normalization(var_0, mean, var, var_4, var_5, 1e-3)
    return var_8
