from functools import partial, wraps

def decorator(func=None, foo='spam'):
    if func is None:
         return partial(decorator, foo=foo)

    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something with `func` and `foo`, if you're so inclined
        pass
    
    return wrapper
