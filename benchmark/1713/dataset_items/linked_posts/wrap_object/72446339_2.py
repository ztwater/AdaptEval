>>> with wrap_object(Foo, "foo") as m:
...     foo = Foo()
...     print(foo.foo())
... 
foo
>>> m.assert_called_once_with()
>>> m.call_count
1
>>> 
