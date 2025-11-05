def meta_wrap(decor):
    @functools.wraps(decor)
    def new_decor(*args, **kwargs):
        if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
            # this is the double-decorated f. 
            # Its first argument should not be a callable
            doubled_f = decor(args[0])
            @functools.wraps(doubled_f)
            def checked_doubled_f(*f_args, **f_kwargs):
                if callable(f_args[0]):
                    raise ValueError('meta_wrap failure: '
                                'first positional argument cannot be callable.')
                return doubled_f(*f_args, **f_kwargs)
            return checked_doubled_f 
        else:
            # decorator arguments
            return lambda real_f: decor(real_f, *args, **kwargs)

    return new_decor
