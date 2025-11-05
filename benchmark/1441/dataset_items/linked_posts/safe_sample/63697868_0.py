import random
from collections import OrderedDict, abc

a = list(range(0, 100))
random.shuffle(a)

# True
a == list(OrderedDict((i, 0) for i in a).keys())

# True
isinstance(OrderedDict().keys(), abc.Set)   
