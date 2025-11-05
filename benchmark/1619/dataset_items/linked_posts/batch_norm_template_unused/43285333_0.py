# Set this to True for training and False for testing
training = tf.placeholder(tf.bool)

x = tf.layers.dense(input_x, units=100)
x = tf.layers.batch_normalization(x, training=training)
x = tf.nn.relu(x)
