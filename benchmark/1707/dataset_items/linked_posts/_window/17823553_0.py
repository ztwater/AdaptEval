>>> n, m = 6, 3
>>> k = n - m+1
>>> print ('{}\n'*(k)).format(*[range(i, i+m) for i in xrange(k)])
[0, 1, 2]
[1, 2, 3]
[2, 3, 4]
[3, 4, 5]
