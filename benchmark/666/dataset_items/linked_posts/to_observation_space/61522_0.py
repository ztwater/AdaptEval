>>> class Foo(object):
...     bar = 'hello'
...     baz = 'world'
...
>>> f = Foo()
>>> [name for name in dir(f) if not name.startswith('__')]
[ 'bar', 'baz' ]
>>> dict((name, getattr(f, name)) for name in dir(f) if not name.startswith('__')) 
{ 'bar': 'hello', 'baz': 'world' }
