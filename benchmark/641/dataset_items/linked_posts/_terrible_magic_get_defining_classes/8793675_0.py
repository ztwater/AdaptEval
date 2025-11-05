import inspect

def my_decorator(f):
    args = inspect.getargspec(f).args
    defined_in_class = bool(args and args[0] == 'self')
    print "%r: %s" %(f, defined_in_class)
