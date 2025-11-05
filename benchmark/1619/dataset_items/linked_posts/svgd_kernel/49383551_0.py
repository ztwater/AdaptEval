def compute_euclidean_distance(x, y):
    size_x = x.shape.dims[0]
    size_y = y.shape.dims[0]
    for i in range(size_x):
        tile_one = tf.reshape(tf.tile(x[i], [size_y]), [size_y, -1])
        eu_one = tf.expand_dims(tf.sqrt(tf.reduce_sum(tf.pow(tf.subtract(tile_one, y), 2), axis=1)), axis=0)
        if i == 0:
            d = eu_one
        else:
            d = tf.concat([d, eu_one], axis=0)
return d
