from decopatch import function_decorator

@function_decorator
def add_tag(tag='hi!'):
    """
    Example decorator to add a 'tag' attribute to a function. 
    :param tag: the 'tag' value to set on the decorated function (default 'hi!).
    """
    def _apply_decorator(f):
        """
        This is the method that will be called when `@add_tag` is used on a 
        function `f`. It should return a replacement for `f`.
        """
        setattr(f, 'tag', tag)
        return f
    return _apply_decorator
