>>> delta()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in delta
ValueError: delta should be called with at least one numerical argument
>>> delta(3)
0
>>> delta('a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in delta
ValueError: delta should only be called with numerical arguments
>>> delta('a', 'b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in delta
ValueError: delta should only be called with numerical arguments
>>> delta('a', 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in delta
ValueError: delta should only be called with numerical arguments
>>> delta(3, 4.5)
1.5
>>> delta(3, 5, 7, 2)
5
