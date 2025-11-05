from mock import patch, MagicMock

class Foo:

    def foo(self):
        return "foo"

class MockFoo(Foo):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Every instance of MockFoo will now have its `foo` method 
        # wrapped in a MagicMock
        self.foo = MagicMock(wraps=self.foo)

with patch("__main__.Foo", MockFoo) as m:
    foo = Foo()
    print(foo.foo())
    assert foo.foo.call_count == 1
