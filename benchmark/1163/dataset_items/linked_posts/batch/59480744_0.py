>>> from types import SimpleNamespace   
>>> d = dict(x=[1, 2], y=['a', 'b'])
>>> ns = SimpleNamespace(**d)
>>> ns.x
[1, 2]
>>> ns
namespace(x=[1, 2], y=['a', 'b'])
