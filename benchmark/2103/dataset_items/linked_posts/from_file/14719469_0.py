>>> class MyClass(object):
...     init = False
...     def __init__(self):
...         print 'init called!'
...         self.init = True
...     def hello(self):
...         print 'hello world!'
... 
>>> class Empty(object):
...     pass
... 
>>> a = MyClass()
init called!
>>> a.hello()
hello world!
>>> print a.init
True
>>> b = Empty()
>>> b.__class__ = MyClass
>>> b.hello()
hello world!
>>> print b.init
False
