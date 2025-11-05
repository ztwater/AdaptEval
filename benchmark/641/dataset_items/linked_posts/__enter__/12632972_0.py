class M(type):
    def __getattr__(*args): return lambda: 0

class X(object):
    __metaclass__ = M

x = X()
type(x).__exit__ # works, returns a lambda

with x: pass # fails, AttributeError
