import functools
import itertools


@functools.total_ordering
class NaturalStringB(str):
    def __repr__(self):
        return "{}({})".format\
            ( type(self).__name__
            , super().__repr__()
            )
    d = lambda s: "".join(c.lower()+c.swapcase() for c in s)
    d = staticmethod(d)
    def __lt__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        groups = map(lambda i: itertools.groupby(i, type(self).isdigit), (self, other))
        zipped = itertools.zip_longest(*groups)
        for s,o in zipped:
            if s is None:
                return True
            if o is None:
                return False
            s_k, s_v = s[0], "".join(s[1])
            o_k, o_v = o[0], "".join(o[1])
            if s_k and o_k:
                s_v, o_v = int(s_v), int(o_v)
                if s_v == o_v:
                    continue
                return s_v < o_v
            elif s_k:
                return True
            elif o_k:
                return False
            else:
                s_v, o_v = self.d(s_v), self.d(o_v)
                if s_v == o_v:
                    continue
                return s_v < o_v
        return False
    def __eq__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        groups = map(lambda i: itertools.groupby(i, type(self).isdigit), (self, other))
        zipped = itertools.zip_longest(*groups)
        for s,o in zipped:
            if s is None or o is None:
                return False
            s_k, s_v = s[0], "".join(s[1])
            o_k, o_v = o[0], "".join(o[1])
            if s_k and o_k:
                s_v, o_v = int(s_v), int(o_v)
                if s_v == o_v:
                    continue
                return False
            elif s_k or o_k:
                return False
            else:
                s_v, o_v = self.d(s_v), self.d(o_v)
                if s_v == o_v:
                    continue
                return False
        return True
    __le__ = object.__le__
    __ne__ = object.__ne__
    __gt__ = object.__gt__
    __ge__ = object.__ge__
