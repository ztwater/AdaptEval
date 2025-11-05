>>> def foo(a: int, b: str, c: typing.List[str] = 3):
...   pass
... 
>>> typing.get_type_hints(foo)
{'a': <class 'int'>, 'b': <class 'str'>, 'c': typing.List[str]}
