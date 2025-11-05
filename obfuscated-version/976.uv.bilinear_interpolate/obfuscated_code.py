def bilinear_interpolate(var_0, var_1, var_2):
    var_1 = np.asarray(var_1)
    var_2 = np.asarray(var_2)

    var_3 = np.floor(x).astype(int)
    var_4 = var_3 + 1
    var_5 = np.floor(y).astype(int)
    var_6 = var_5 + 1

    var_3 = np.clip(var_3, 0, var_0.shape[1]-1);
    var_4 = np.clip(var_4, 0, var_0.shape[1]-1);
    var_5 = np.clip(var_5, 0, var_0.shape[0]-1);
    var_6 = np.clip(var_6, 0, var_0.shape[0]-1);

    var_7 = var_0[ var_5, var_3 ]
    var_8 = var_0[ var_6, var_3 ]
    var_9 = var_0[ var_5, var_4 ]
    var_10 = var_0[ var_6, var_4 ]

    var_11 = (var_4-var_1) * (var_6-var_2)
    var_12 = (var_4-var_1) * (var_2-var_5)
    var_13 = (var_1-var_3) * (var_6-var_2)
    var_14 = (var_1-var_3) * (var_2-var_5)

    return var_11*var_7 + var_12*var_8 + var_13*var_9 + var_14*var_10
