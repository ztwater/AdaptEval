def isnamedtupleinstance(var_0):
    var_1 = type(var_0)
    var_2 = var_1.__bases__
    if len(var_2) != 1 or var_2[0] != tuple: return False
    var_3 = getattr(var_1, '_fields', None)
    if not isinstance(var_3, tuple): return False
    return all(type(n)==str for n in var_3)
