>>> class A(object):
...   def __init__(self):
...     self.b = 1
...     self.c = 2
...   def do_nothing(self):
...     pass
...
>>> a = A()
>>> a.__dict__
{'c': 2, 'b': 1}
