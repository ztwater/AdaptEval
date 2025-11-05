def split(var_0, var_1):
    k, m = divmod(len(var_0), var_1)
    return (var_0[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(var_1))
