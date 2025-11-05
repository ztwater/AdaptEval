def min_sparse(var_0):
    if len(var_0.data) == 0:
        return 0
    var_1 = var_0.data.min()
    return var_1 if var_0.getnnz() == var_0.size else min(var_1, 0)
