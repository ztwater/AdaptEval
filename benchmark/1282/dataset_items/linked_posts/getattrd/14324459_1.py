>>> getattrd(int, 'a')
AttributeError: type object 'int' has no attribute 'a'

>>> getattr(int, 'a')
AttributeError: type object 'int' has no attribute 'a'

>>> getattrd(int, 'a', None)
None

>>> getattr(int, 'a', None)
None

>>> getattrd(int, 'a', None)
None

>>> getattrd(int, '__class__.__name__')
type

>>> getattrd(int, '__class__')
<type 'type'>
