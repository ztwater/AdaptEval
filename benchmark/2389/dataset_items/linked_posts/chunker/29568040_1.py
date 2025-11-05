>>> def foo():
...     i = 0
...     while True:
...         i += 1
...         yield i
...
>>> c = chunks(foo(), 3)
>>> c.next()
(1, 2, 3)
>>> c.next()
(4, 5, 6)
>>> list(chunks('abcdefg', 2))
[('a', 'b'), ('c', 'd'), ('e', 'f')]
