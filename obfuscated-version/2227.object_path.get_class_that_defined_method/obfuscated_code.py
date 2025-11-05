def get_class_that_defined_method(var_0):
    if isinstance(var_0, functools.partial):
        return get_class_that_defined_method(var_0.func)
    if inspect.ismethod(var_0) or (inspect.isbuiltin(var_0) and getattr(var_0, '__self__', None) is not None and getattr(var_0.__self__, '__class__', None)):
        for cls in inspect.getmro(var_0.__self__.__class__):
            if var_0.__name__ in cls.__dict__:
                return cls
        var_0 = getattr(var_0, '__func__', var_0)  # fallback to __qualname__ parsing
    if inspect.isfunction(var_0):
        var_1 = getattr(inspect.getmodule(var_0),
                      var_0.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                      None)
        if isinstance(var_1, type):
            return var_1
    return getattr(var_0, '__objclass__', None)  # handle special descriptor objects
