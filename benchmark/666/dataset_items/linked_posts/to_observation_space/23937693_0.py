class A(object):
    def __init__(self):
        self.b = 1
        self.c = 2
    def __getitem__(self, item):
        return self.__dict__[item]

# Usage: 
a = A()
a.__getitem__('b')  # Outputs 1
a.__dict__  # Outputs {'c': 2, 'b': 1}
vars(a)  # Outputs {'c': 2, 'b': 1}
