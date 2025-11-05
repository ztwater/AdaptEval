@numba.njit
def repeat_blocks_jit(var_0, var_1, var_2):
    var_3 = np.empty((sizes * repeats).sum(), var_0.dtype)
    var_4 = 0
    var_5 = 0
    for i, size in enumerate(var_1):
        var_6 = var_4 + size
        for rep in range(var_2[i]):
            var_7 = var_5 + size
            var_3[var_5:var_7] = var_0[var_4:var_6]
            var_5 = var_7
        var_4 = var_6
    return var_3
