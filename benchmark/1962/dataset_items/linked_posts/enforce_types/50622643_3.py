>>> isinstance(typing.Union, typing._SpecialForm)
True
>>> isinstance(typing.Union[int, str], typing._SpecialForm)
False
>>> typing.get_origin(typing.Union[int, str])
typing.Union
