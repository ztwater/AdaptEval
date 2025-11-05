sess = tf.InteractiveSession()
layer1_weights = tf.Variable(tf.truncated_normal(
  [patch_size, patch_size, num_channels, depth], stddev=0.1),name="layer1_weights")
tf.train.Saver().restore(sess, "/tmp/model.ckpt")
