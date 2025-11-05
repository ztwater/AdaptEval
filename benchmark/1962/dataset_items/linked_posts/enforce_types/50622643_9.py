>>> def foo(a: int, b: str, c: typing.List[str] = None):
...   pass
... 
>>> typing.get_type_hints(foo)
{'a': <class 'int'>, 'b': <class 'str'>, 'c': typing.Union[typing.List[str], NoneType]}
