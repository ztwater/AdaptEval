def new_getfile(var_0, var_1=inspect.getfile):
    if not inspect.isclass(var_0):
        return var_1(var_0)
    
    # Lookup by parent module (as in current inspect)
    if hasattr(var_0, '__module__'):
        var_2 = sys.modules.get(var_0.__module__)
        if hasattr(var_2, '__file__'):
            return var_2.__file__
    
    # If parent module is __main__, lookup by methods (NEW)
    for name, member in inspect.getmembers(var_0):
        if inspect.isfunction(member) and var_0.__qualname__ + '.' + member.__name__ == member.__qualname__:
            return inspect.getfile(member)
    else:
        raise TypeError('Source for {!r} not found'.format(var_0))
