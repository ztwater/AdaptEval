>>> from itertools import takewhile, izip
>>> ''.join(c[0] for c in takewhile(lambda x: all(x[0] == y for y in x), izip(*strings)))
'my_prefix_'
