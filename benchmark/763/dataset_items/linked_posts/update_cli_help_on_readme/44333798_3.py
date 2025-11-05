In [176]: def foo(x,y):
     ...:     return x,y
     ...: 
In [177]: bar = lambda y: foo('x_str',y)
In [178]: bar('y_str')
Out[178]: ('x_str', 'y_str')
