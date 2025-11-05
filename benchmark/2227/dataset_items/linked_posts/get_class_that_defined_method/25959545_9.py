if inspect.ismethoddescriptor(meth):
    return getattr(meth, '__objclass__', None)
