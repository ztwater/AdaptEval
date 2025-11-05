>>> def foo(bar: str, baz: list, spam: str = 'eggs', *, monty: str = 'python', **kw) -> None: pass
... 
>>> import inspect
>>> inspect.getfullargspec(foo)
FullArgSpec(args=['bar', 'baz', 'spam'], varargs=None, varkw='kw', defaults=('eggs',), kwonlyargs=['monty'], kwonlydefaults={'monty': 'python'}, annotations={'baz': <class 'list'>, 'return': None, 'spam': <class 'str'>, 'monty': <class 'str'>, 'bar': <class 'str'>})
