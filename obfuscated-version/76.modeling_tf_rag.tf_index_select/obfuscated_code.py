def tf_index_select(var_0, var_1, var_2):
    """
    input_(tensor): input tensor
    dim(int): dimension
    indices(list): selected indices list
    """
    var_3 = var_0.get_shape().as_list()
    if var_1 == -1:
        var_1 = len(var_3)-1
    var_3[var_1] = 1
    
    var_4 = []
    for idx in var_2:
        var_5 = [0]*len(var_3)
        var_5[var_1] = idx
        var_4.append(tf.slice(var_0, var_5, var_3))
    var_6 = tf.concat(var_4, axis=var_1)
    
    return var_6
