>>> from collections import OrderedDict
>>> items = [1, 2, 0, 1, 3, 2]
>>> list(OrderedDict.fromkeys(items))
[1, 2, 0, 3]
