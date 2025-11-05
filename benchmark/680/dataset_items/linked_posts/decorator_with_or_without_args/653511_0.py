from functools import wraps
import inspect

def redirect_output(fn_or_output):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **args):
            # Redirect output
            try:
                return fn(*args, **args)
            finally:
                # Restore output
        return wrapper

    if inspect.isfunction(fn_or_output):
        # Called with no parameter
        return decorator(fn_or_output)
    else:
        # Called with a parameter
        return decorator
