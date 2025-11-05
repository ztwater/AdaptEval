
import tensorflow as tf
import torch
import numpy as np

a = np.arange(2*3*4).reshape(2,3,4)
dim = 1
indices = [0,2]
# array([[[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7],
#         [ 8,  9, 10, 11]],

#        [[12, 13, 14, 15],
#         [16, 17, 18, 19],
#         [20, 21, 22, 23]]])

# pytorch
res = torch.tensor(a).index_select(dim, torch.tensor(indices))
# tensor([[[ 0,  1,  2,  3],
#          [ 8,  9, 10, 11]],

#         [[12, 13, 14, 15],
#          [20, 21, 22, 23]]])

# tensorflow
res = tf_index_select(tf.constant(a), dim, indices)
# tensor([[[ 0,  1,  2,  3],
#          [ 8,  9, 10, 11]],

#         [[12, 13, 14, 15],
#          [20, 21, 22, 23]]])
