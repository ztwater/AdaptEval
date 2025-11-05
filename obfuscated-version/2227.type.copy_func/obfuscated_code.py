import copy
import types
import functools

def copy_func(var_0, var_1=None, var_2=None):
    """Based on https://stackoverflow.com/a/13503277/2988730 (@unutbu)"""
    if var_1 is None:
        var_1 = var_0.__globals__
    var_3 = types.FunctionType(var_0.__code__, var_1, name=var_0.__name__,
                           argdefs=var_0.__defaults__, closure=var_0.__closure__)
    var_3 = functools.update_wrapper(var_3, var_0)
    if var_2 is not None:
        var_3.__module__ = var_2
    var_3.__kwdefaults__ = copy.copy(var_0.__kwdefaults__)
    return var_3
