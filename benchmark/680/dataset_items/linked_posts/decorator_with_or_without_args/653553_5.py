def redirect_output(file = sys.stderr):
    def decorator(file, f):
        def df(*args, **kwargs):
            print 'redirecting to ', file
            return f(*args, **kwargs)
        return df
    return lambda f: decorator(file, f)
