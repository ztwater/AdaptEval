def __getattr__(self, name):
    if '.' in name:
        group,name = name.split('.',1)
        try:
            ns = self.__dict__[group]
        except KeyError:
            raise AttributeError
        return getattr(ns, name)
    else:
        raise AttributeError
