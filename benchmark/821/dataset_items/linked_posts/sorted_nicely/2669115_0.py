In [4]: a = set(['booklet', '4 sheets', '48 sheets', '12 sheets'])

In [5]: def f(x):
   ...:     num = x.split(None, 1)[0]
   ...:     if num.isdigit():
   ...:         return int(num)
   ...:     return x
   ...: 

In [6]: sorted(a, key=f)
Out[6]: ['4 sheets', '12 sheets', '48 sheets', 'booklet']
