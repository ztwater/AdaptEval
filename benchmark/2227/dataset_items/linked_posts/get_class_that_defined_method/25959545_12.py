if inspect.ismethod(meth) or (inspect.isbuiltin(meth) and getattr(meth, '__self__', None) and getattr(meth.__self__, '__class__', None)):
    # ordinary method handling
