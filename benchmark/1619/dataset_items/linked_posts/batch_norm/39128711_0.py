batch_norm = tf.cond(is_train, 
    lambda: tf.contrib.layers.batch_norm(prev, activation_fn=tf.nn.relu, is_training=True, reuse=None),
    lambda: tf.contrib.layers.batch_norm(prev, activation_fn =tf.nn.relu, is_training=False, reuse=True))
