import functools
import itertools


@functools.total_ordering
class NaturalStringA(str):
    def __repr__(self):
        return "{}({})".format\
            ( type(self).__name__
            , super().__repr__()
            )
    d = lambda c, s: [ c.NaturalStringPart("".join(v))
                        for k,v in
                       itertools.groupby(s, c.isdigit)
                     ]
    d = classmethod(d)
    @functools.total_ordering
    class NaturalStringPart(str):
        d = lambda s: "".join(c.lower()+c.swapcase() for c in s)
        d = staticmethod(d)
        def __lt__(self, other):
            if not isinstance(self, type(other)):
                return NotImplemented
            try:
                return int(self) < int(other)
            except ValueError:
                if self.isdigit():
                    return True
                elif other.isdigit():
                    return False
                else:
                    return self.d(self) < self.d(other)
        def __eq__(self, other):
            if not isinstance(self, type(other)):
                return NotImplemented
            try:
                return int(self) == int(other)
            except ValueError:
                if self.isdigit() or other.isdigit():
                    return False
                else:
                    return self.d(self) == self.d(other)
        __le__ = object.__le__
        __ne__ = object.__ne__
        __gt__ = object.__gt__
        __ge__ = object.__ge__
    def __lt__(self, other):
        return self.d(self) < self.d(other)
    def __eq__(self, other):
        return self.d(self) == self.d(other)
    __le__ = object.__le__
    __ne__ = object.__ne__
    __gt__ = object.__gt__
    __ge__ = object.__ge__
