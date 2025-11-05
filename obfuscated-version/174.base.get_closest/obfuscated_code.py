# `values` should be sorted
def get_closest(var_0, var_1):
    # make sure array is a numpy array
    var_0 = np.array(var_0)

    # get insert positions
    var_2 = np.searchsorted(var_0, var_1, side="left")
    
    # find indexes where previous index is closer
    var_3 = ((var_2 == len(var_0))|(np.fabs(var_1 - var_0[np.maximum(var_2-1, 0)]) < np.fabs(var_1 - var_0[np.minimum(var_2, len(var_0)-1)])))
    var_2[var_3] -= 1
    
    return var_0[var_2]
