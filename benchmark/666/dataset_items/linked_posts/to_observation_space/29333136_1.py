def iterable(cls):
    def iterfn(self):
        iters = dict((x,y) for x,y in cls.__dict__.items() if x[:2] != '__')
        iters.update(self.__dict__)

        for x,y in iters.items():
            yield x,y

    cls.__iter__ = iterfn
    return cls

@iterable
class B(object):
    d = 'd'
    e = 'e'
    f = 'f'

    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        self.c = 'c'

b = B()
print(dict(b))
