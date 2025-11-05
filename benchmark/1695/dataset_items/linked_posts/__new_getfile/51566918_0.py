...
if isclass(object):
    if hasattr(object, '__module__'):
        object = sys.modules.get(object.__module__)
        if hasattr(object, '__file__'):
            return object.__file__
    raise TypeError('{!r} is a built-in class'.format(object))
...
