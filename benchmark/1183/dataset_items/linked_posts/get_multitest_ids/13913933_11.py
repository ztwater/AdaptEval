>>> def spam(x):
...     def eggs():
...         return x
...     return eggs
... 
>>> spam(1).__code__.co_freevars
('x',)
>>> spam(1)()
1
>>> spam(1).__closure__
>>> spam(1).__closure__[0].cell_contents
1
>>> spam(5).__closure__[0].cell_contents
5
