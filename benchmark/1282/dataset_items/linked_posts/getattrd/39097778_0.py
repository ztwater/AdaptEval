>>> import operator
>>> class B():
...   c = 'foo'
... 
>>> class A():
...   b = B()
... 
>>> a = A()
>>> operator.attrgetter('b.c')(a)
'foo'
