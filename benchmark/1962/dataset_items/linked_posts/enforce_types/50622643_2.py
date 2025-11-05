# Python 3.8
>>> import typing
>>> typing.get_origin(typing.List)
<class 'list'>
>>> typing.get_origin(typing.List[int])
<class 'list'>
