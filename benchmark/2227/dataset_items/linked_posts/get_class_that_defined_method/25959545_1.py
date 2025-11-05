def get_class_that_defined_method(meth):
    # meth must be a bound method
    if inspect.ismethod(meth):
        for cls in inspect.getmro(meth.__self__.__class__):
            if meth.__name__ in cls.__dict__:
                return cls
    return None  # not required since None would have been implicitly returned anyway
