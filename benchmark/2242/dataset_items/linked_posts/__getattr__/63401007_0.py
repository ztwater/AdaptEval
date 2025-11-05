class A:
    pass
a = A()
a.__getattr__ # error
a.__getattribute__ # return a method-wrapper
