# import numpy as np
import tensorflow as tf

# last-axis gathering only - use 2D-reshape-trick for Torch's style nD gathering
def torch_gather(param, id_tensor):
    # 2d-gather torch equivalent: https://stackoverflow.com/questions/52129909/tensorflow-equivalent-of-torch-gather
    def gather2d(target, id_tensor):
        # idx = tf.stack([tf.range(tf.shape(id_tensor)[0]), id_tensor[:, 0]], axis=-1)
        idx = tf.stack([tf.range(tf.shape(id_tensor)[0], dtype=id_tensor.dtype), id_tensor[:, 0]], axis=-1)
        result = tf.gather_nd(target, idx)
        return tf.expand_dims(result, axis=-1)

    target = tf.reshape(param, (-1, param.shape[-1]))  # reshape 2D
    # print(target)
    target_shape = id_tensor.shape

    id_tensor = tf.reshape(id_tensor, (-1, 1))  # also 2D-index
    # print(id_tensor)
    result = gather2d(target, id_tensor)
    # print(result)
    return tf.reshape(result, target_shape)

