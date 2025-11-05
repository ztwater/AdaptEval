def get_all_subclasses(cls):
    """ Generator of all a class's subclasses. """
    try:
        for subclass in cls.__subclasses__():
            yield subclass
            for subclass in get_all_subclasses(subclass):
                yield subclass
    except TypeError:
        return

def all_subclasses3(classname):
    for cls in get_all_subclasses(object):  # object is base of all new-style classes.
        if cls.__name__.split('.')[-1] == classname:
            break
    else:
        raise ValueError('class %s not found' % classname)
    direct_subclasses = cls.__subclasses__()
    return direct_subclasses + [g for s in direct_subclasses
                                    for g in all_subclasses3(s.__name__)]

# no eval('xxx')
def func3():
    print(all_subclasses3('Foo'))

func3()  # Also works
# -> [<class '__main__.Bar'>, <class '__main__.Baz'>, <class '__main__.Bing'>]
