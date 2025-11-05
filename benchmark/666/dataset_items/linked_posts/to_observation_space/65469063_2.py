>>> foo = Foo()
>>> foo.a = 1
>>> foo.b = 2
>>> instance_attributes(foo)
{'a': 1, 'b': 2}

>>> bar = Bar()
>>> bar.a = 3
>>> instance_attributes(bar)
{'a': 3}

>>> instance_attributes("baz") 
{}

