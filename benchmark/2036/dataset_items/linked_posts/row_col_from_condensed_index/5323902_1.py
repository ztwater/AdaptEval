In []: def f(n, c):
   ..:     n= ceil(sqrt(2* n))
   ..:     ti= triu_indices(n, 1)
   ..:     return ti[0][c]+ 1, ti[1][c]+ 1
   ..:
In []: f(len(c), 5)
Out[]: (2, 4)
