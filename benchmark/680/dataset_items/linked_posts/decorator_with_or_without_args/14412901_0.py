def decorator(*args, **kwargs):
    if len(args) == 1 and len(kwargs) == 0 and callable(args[0]):
        # called as @decorator
    else:
        # called as @decorator(*args, **kwargs)
