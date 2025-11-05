>>> from collections import defaultdict
>>> d = defaultdict(lambda : defaultdict(int))
>>> print d[0]
defaultdict(<type 'int'>, {})
>>> print d[0]["x"]
0
