>>> import inspect
>>> def foo(): pass
... 
>>> inspect.isfunction(foo)
True
>>> inspect.ismethod(foo)
False
>>> class C(object):
...     def foo(self):
...             pass
... 
>>> inspect.isfunction(C.foo)
False
>>> inspect.ismethod(C.foo)
True
>>> inspect.isfunction(C().foo)
False
>>> inspect.ismethod(C().foo)
True
