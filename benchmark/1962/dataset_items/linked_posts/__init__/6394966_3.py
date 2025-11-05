def wrapper(f):

    memoize = memoized(f)

    @functools.wraps(f)
    def helper(*args, **kws):
        return memoize(*args, **kws)

    return helper


@wrapper
def fibonacci(n):
    """fibonacci docstring"""
    if n <= 1:
       return n
    return fibonacci(n-1) + fibonacci(n-2)
