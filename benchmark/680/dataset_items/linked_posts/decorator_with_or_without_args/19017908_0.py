from functools import wraps

def custom_decorator(function=None, some_arg=None, some_other_arg=None):
    def actual_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Do stuff with args here...
            if some_arg:
                print(some_arg)
            if some_other_arg:
                print(some_other_arg)
            return f(*args, **kwargs)
        return wrapper
    if function:
        return actual_decorator(function)
    return actual_decorator
