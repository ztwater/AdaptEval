>>> fn('1')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fn
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> fn(1, '2')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fn
TypeError: '>' not supported between instances of 'str' and 'int'
>>> fn('a', 'b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fn
TypeError: unsupported operand type(s) for -: 'str' and 'str'
