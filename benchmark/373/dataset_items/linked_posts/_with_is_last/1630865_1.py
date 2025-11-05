>>> def do_every(x): print "E", x
...
>>> def do_between(x): print "B", x
...
>>> test_input = iter(range(5))
>>>
>>> from itertools import tee, izip
>>>
>>> items, between = tee(test_input, 2)
>>> first = items.next()
>>> do_every(first)
E 0
>>> for i,b in izip(items, between):
...     do_between(b)
...     do_every(i)
...
B 0
E 1
B 1
E 2
B 2
E 3
B 3
E 4
>>>
