if isinstance(meth, functools.partial):
    return get_class_that_defined_method(meth.func)
