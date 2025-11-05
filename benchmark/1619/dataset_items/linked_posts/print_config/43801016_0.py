np.sum([np.prod(v.get_shape().as_list()) for v in tf.trainable_variables()])
