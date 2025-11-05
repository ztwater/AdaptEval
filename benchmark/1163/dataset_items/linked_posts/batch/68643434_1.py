dct = dict(a=1)
dot_dct = DotDict(b=2)
foo = {c: i for i, c in enumerate('xyz')}
for d in (dct, dot_dct):
    # you would have to use dct.update and dot_dct.__update methods
    dict.update(d, foo)
    
assert dict.get(dot, 'foo', 0) is 0
