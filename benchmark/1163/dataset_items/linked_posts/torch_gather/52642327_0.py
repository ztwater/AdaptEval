# a.shape (16L, 10L)
# idx.shape (16L,1)
idx = tf.stack([tf.range(tf.shape(idx)[0]),idx[:,0]],axis=-1)
b = tf.gather_nd(a,idx)
