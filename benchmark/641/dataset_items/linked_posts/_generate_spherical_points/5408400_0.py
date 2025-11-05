In []: p= 2* rand(3, 1e4)- 1
In []: p= p[:, sum(p* p, 0)** .5<= 1]
In []: p.shape
Out[]: (3, 5216)
