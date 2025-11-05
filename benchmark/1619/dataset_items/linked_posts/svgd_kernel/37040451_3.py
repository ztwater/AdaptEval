A = tf.constant([[1, 1], [2, 2], [3, 3]])
r = tf.reduce_sum(A*A, 1)

# turn r into column vector
r = tf.reshape(r, [-1, 1])
D = r - 2*tf.matmul(A, tf.transpose(A)) + tf.transpose(r)
sess = tf.Session()
sess.run(D)
