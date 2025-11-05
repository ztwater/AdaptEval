def enforce_types(var_0):
    var_1 = inspect.getfullargspec(var_0)

    def check_types(*var_2, **var_3):
        var_4 = dict(zip(var_1.args, var_2))
        var_4.update(var_3)
        for name, value in var_4.items():
            with suppress(KeyError):  # Assume un-annotated parameters can be any type
                var_5 = var_1.annotations[name]
                if isinstance(var_5, typing._SpecialForm):
                    # No check for typing.Any, typing.Union, typing.ClassVar (without parameters)
                    continue
                try:
                    var_6 = var_5.__origin__
                except AttributeError:
                    # In case of non-typing types (such as <class 'int'>, for instance)
                    var_6 = var_5
                # In Python 3.8 one would replace the try/except with
                # actual_type = typing.get_origin(type_hint) or type_hint
                if isinstance(var_6, typing._SpecialForm):
                    # case of typing.Union[…] or typing.ClassVar[…]
                    var_6 = var_5.__args__

                if not isinstance(value, var_6):
                    raise TypeError('Unexpected type for \'{}\' (expected {} but found {})'.format(name, var_5, type(value)))

    def decorate(var_7):
        @wraps(func)
        def wrapper(*var_2, **var_3):
            check_types(*var_2, **var_3)
            return var_7(*var_2, **var_3)
        return wrapper

    if inspect.isclass(var_0):
        var_0.__init__ = decorate(var_0.__init__)
        return var_0

    return decorate(var_0)
