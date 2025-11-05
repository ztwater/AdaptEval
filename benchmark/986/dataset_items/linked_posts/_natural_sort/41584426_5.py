import functools
import itertools
import enum


class OrderingType(enum.Enum):
    PerWordSwapCase         = lambda s: s.lower()+s.swapcase()
    PerCharacterSwapCase    = lambda s: "".join(c.lower()+c.swapcase() for c in s)


class NaturalOrdering:
    @classmethod
    def by(cls, ordering):
        def wrapper(string):
            return cls(string, ordering)
        return wrapper
    def __init__(self, string, ordering=OrderingType.PerCharacterSwapCase):
        self.string = string
        self.groups = [ (k,int("".join(v)))
                            if k else
                        (k,ordering("".join(v)))
                            for k,v in
                        itertools.groupby(string, str.isdigit)
                      ]
    def __repr__(self):
        return "{}({})".format\
            ( type(self).__name__
            , self.string
            )
    def __lesser(self, other, default):
        if not isinstance(self, type(other)):
            return NotImplemented
        for s,o in itertools.zip_longest(self.groups, other.groups):
            if s is None:
                return True
            if o is None:
                return False
            s_k, s_v = s
            o_k, o_v = o
            if s_k and o_k:
                if s_v == o_v:
                    continue
                return s_v < o_v
            elif s_k:
                return True
            elif o_k:
                return False
            else:
                if s_v == o_v:
                    continue
                return s_v < o_v
        return default
    def __lt__(self, other):
        return self.__lesser(other, default=False)
    def __le__(self, other):
        return self.__lesser(other, default=True)
    def __eq__(self, other):
        if not isinstance(self, type(other)):
            return NotImplemented
        for s,o in itertools.zip_longest(self.groups, other.groups):
            if s is None or o is None:
                return False
            s_k, s_v = s
            o_k, o_v = o
            if s_k and o_k:
                if s_v == o_v:
                    continue
                return False
            elif s_k or o_k:
                return False
            else:
                if s_v == o_v:
                    continue
                return False
        return True
    # functools.total_ordering doesn't create single-call wrappers if both
    # __le__ and __lt__ exist, so do it manually.
    def __gt__(self, other):
        op_result = self.__le__(other)
        if op_result is NotImplemented:
            return op_result
        return not op_result
    def __ge__(self, other):
        op_result = self.__lt__(other)
        if op_result is NotImplemented:
            return op_result
        return not op_result
    # __ne__ is the only implied ordering relationship, it automatically
    # delegates to __eq__
