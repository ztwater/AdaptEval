>>> for i in chunker('12345', 2):
...     print(repr(i))
...
('1', '2')
('3', '4')
>>> for i in chunker('12345', 2, ''.join):
...     print(repr(i))
...
'12'
'34'
