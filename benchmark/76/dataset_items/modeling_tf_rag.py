import os
import sys
import tensorflow as tf

from transformers.modeling_tf_utils import shape_list

def tf_index_select(input_, dim, indices):
    """
    Input:
        input_(tensor): input tensor dim(int): dimension indices(list): selected indices list
    Output:
        mimic of torch_tensor.index_select(dim, indices)

    credit: https://stackoverflow.com/questions/58464790/is-there-an-equivalent-function-of-pytorch-named-index-select-in-tensorflow
    """
    # shape = input_.get_shape().as_list()
    shape = shape_list(input_)
    if dim == -1:
        dim = len(shape) - 1
    shape[dim] = 1

    tmp = []
    for idx in indices:
        begin = [0] * len(shape)
        begin[dim] = idx
        tmp.append(tf.slice(input_, begin, shape))
    res = tf.concat(tmp, axis=dim)

    return res

