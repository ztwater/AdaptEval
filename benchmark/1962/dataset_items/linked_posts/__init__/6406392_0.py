import functools
import types

class CallableClassDecorator:
    """Base class that extracts attributes and assigns them to self.

    By default the extracted attributes are:
         ['__doc__', '__name__', '__module__'].
    """

    def __init__(self, wrapped, assigned=functools.WRAPPER_ASSIGNMENTS):
        for attr in assigned:
            setattr(self, attr, getattr(wrapped, attr))
        super().__init__()

    def __get__(self, obj, objtype):
        return types.MethodType(self.__call__, obj)
