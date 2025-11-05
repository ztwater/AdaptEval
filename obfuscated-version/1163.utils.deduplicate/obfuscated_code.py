def f7(var_0):
    var_1 = set()
    var_2 = var_1.add
    return [x for x in var_0 if not (x in var_1 or var_2(x))]
