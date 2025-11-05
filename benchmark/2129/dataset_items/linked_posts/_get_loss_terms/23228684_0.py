>>> def foo(bar, baz, spam='eggs', **kw): pass
... 
>>> import inspect
>>> inspect.getargspec(foo)
ArgSpec(args=['bar', 'baz', 'spam'], varargs=None, keywords='kw', defaults=('eggs',))
>>> inspect.getargspec(foo).args
['bar', 'baz', 'spam']
