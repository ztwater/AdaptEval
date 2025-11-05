In [4]: glom(data, "a.b.foo")
---------------------------------------------------------------------------
PathAccessError                           Traceback (most recent call last)
<ipython-input-4-2a3467493ac4> in <module>
----> 1 glom(data, "a.b.foo")

~/.cache/pypoetry/virtualenvs/neural-knapsack-dE7ihQtM-py3.8/lib/python3.8/site-packages/glom/core.py in glom(target, spec, **kwargs)
   2179 
   2180     if err:
-> 2181         raise err
   2182     return ret
   2183 

PathAccessError: error raised while processing, details below.
 Target-spec trace (most recent last):
 - Target: {'a': {'b': {'c': 'd'}}}
 - Spec: 'a.b.foo'
glom.core.PathAccessError: could not access 'foo', part 2 of Path('a', 'b', 'foo'), got error: KeyError('foo')
