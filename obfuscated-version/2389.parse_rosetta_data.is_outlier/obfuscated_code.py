def reject_outliers(var_0, var_1 = 2.):
    var_2 = np.abs(var_0 - np.median(var_0))
    var_3 = np.median(var_2)
    var_4 = var_2 / var_3 if var_3 else np.zeros(len(var_2))
    return var_0[var_4<var_1]
