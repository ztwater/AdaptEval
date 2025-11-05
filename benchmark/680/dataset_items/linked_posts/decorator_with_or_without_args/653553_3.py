import types
def redirect_output(arg):
    def decorator(file, f):
        def df(*args, **kwargs):
            print 'redirecting to ', file
            return f(*args, **kwargs)
        return df
    if type(arg) is types.FunctionType:
        return decorator(sys.stderr, arg)
    return lambda f: decorator(arg, f)
