from decopatch import function_decorator, DECORATED

@function_decorator
def add_tag(tag='hi!', f=DECORATED):
    """
    Example decorator to add a 'tag' attribute to a function.
    :param tag: the 'tag' value to set on the decorated function (default 'hi!).
    """
    setattr(f, 'tag', tag)
    return f
