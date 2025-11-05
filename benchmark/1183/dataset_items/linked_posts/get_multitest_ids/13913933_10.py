>>> foo.__code__.co_cellvars               # foo function `x`
('x',)
>>> foo.__code__.co_consts[2].co_cellvars  # Foo class, no cell variables
()
>>> foo.__code__.co_consts[2].co_consts[2].co_freevars  # Refers to `x` in foo
('x',)
>>> foo().y
[2]
