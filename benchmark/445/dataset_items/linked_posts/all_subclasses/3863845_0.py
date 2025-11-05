def traced_subclass(baseclass):
    class _SubclassTracer(type):
        def __new__(cls, classname, bases, classdict):
            obj = type(classname, bases, classdict)
            if baseclass in bases: # sanity check
                attrname = '_%s__derived' % baseclass.__name__
                derived = getattr(baseclass, attrname, {})
                derived.update( {classname:obj} )
                setattr(baseclass, attrname, derived)
             return obj
    return _SubclassTracer

def subclasses(baseclass):
    attrname = '_%s__derived' % baseclass.__name__
    return getattr(baseclass, attrname, None)


class BaseClass(object):
    pass

class SubclassA(BaseClass):
    __metaclass__ = traced_subclass(BaseClass)

class SubclassB(BaseClass):
    __metaclass__ = traced_subclass(BaseClass)

print subclasses(BaseClass)
