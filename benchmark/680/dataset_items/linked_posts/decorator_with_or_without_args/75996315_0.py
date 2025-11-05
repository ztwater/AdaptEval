from functools import wraps, partial

def with_optional_params(decorator):
    return wraps(decorator)(
        lambda func=None, /, **kwargs: partial(decorator, **kwargs)
        if func is None
        else decorator(func, **kwargs)
    )

@with_optional_params
def printed(func, *, pre=True, post=True):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if pre:
            print('pre')
        result = func(*args, **kwargs)
        if post:
            print('post')
        return result
    return wrapper

@printed
def foo(): pass

@printed(post=False)
def foo(): pass
