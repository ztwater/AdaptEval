# Python 3.7
>>> typing.Union[int, str].__args__
(<class 'int'>, <class 'str'>)

# Python 3.8
>>> typing.get_args(typing.Union[int, str])
(<class 'int'>, <class 'str'>)
