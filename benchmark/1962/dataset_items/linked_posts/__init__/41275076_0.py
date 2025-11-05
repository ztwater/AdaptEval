def wrap_is_timeout(base):
    '''Adds `.is_timeout=True` attribute to objects returned by `base()`.

    When `base` is class, it returns a subclass with same name and adds read-only property.
    Otherwise, it returns a function that sets `.is_timeout` attribute on result of `base()` call.

    Wrappers make best effort to be transparent.
    '''
    if inspect.isclass(base):
        class wrapped(base):
            is_timeout = property(lambda _: True)

        for k in functools.WRAPPER_ASSIGNMENTS:
            v = getattr(base, k, _MISSING)
            if v is not _MISSING:
                try:
                    setattr(wrapped, k, v)
                except AttributeError:
                    pass
        return wrapped

    @functools.wraps(base)
    def fun(*args, **kwargs):
        ex = base(*args, **kwargs)
        ex.is_timeout = True
        return ex
    return fun
