        # last-axis gathering only - use 2D-reshape-trick for Torch's style nD gathering
        def torch_gather(var_0, var_1):

            # 2d-gather torch equivalent from @LiShaoyuan above 
            def gather2d(var_2, var_1):
                var_3 = tf.stack([tf.range(tf.shape(var_1)[0]),var_1[:,0]],axis=-1)
                var_4 = tf.gather_nd(var_2,var_3)
                return tf.expand_dims(var_4,axis=-1)

            var_2 = tf.reshape(var_0, (-1, var_0.shape[-1])) # reshape 2D
            var_5 = var_1.shape

            var_1 = tf.reshape(var_1, (-1, 1)) # also 2D-index
            var_4 = gather2d(var_2, var_1)
            return tf.reshape(var_4, var_5)
