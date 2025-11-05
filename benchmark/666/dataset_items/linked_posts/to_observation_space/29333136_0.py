class A(object):
    d = '4'
    e = '5'
    f = '6'

    def __init__(self):
        self.a = '1'
        self.b = '2'
        self.c = '3'

    def __iter__(self):
        # first start by grabbing the Class items
        iters = dict((x,y) for x,y in A.__dict__.items() if x[:2] != '__')

        # then update the class items with the instance items
        iters.update(self.__dict__)

        # now 'yield' through the items
        for x,y in iters.items():
            yield x,y

a = A()
print(dict(a)) 
# prints "{'a': '1', 'c': '3', 'b': '2', 'e': '5', 'd': '4', 'f': '6'}"
