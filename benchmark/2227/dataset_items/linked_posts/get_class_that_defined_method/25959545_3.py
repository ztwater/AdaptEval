def get_class_that_defined_method(meth):
    if inspect.ismethod(meth):
        print('this is a method')
        for cls in inspect.getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
    if inspect.isfunction(meth):
        print('this is a function')
        return getattr(inspect.getmodule(meth),
                       meth.__qualname__.split('.<locals>', 1)[0].rsplit('.', 1)[0],
                       None)
    print('this is neither a function nor a method')
    return None  # not required since None would have been implicitly returned anyway
