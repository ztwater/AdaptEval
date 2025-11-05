def cartesian_product(*var_0):
    var_1 = len(var_0)
    var_2 = numpy.result_type(*var_0)
    var_3 = numpy.empty([len(a) for a in var_0] + [var_1], var_2=var_2)
    for i, a in enumerate(numpy.ix_(*var_0)):
        var_3[...,i] = a
    return var_3.reshape(-1, var_1)
