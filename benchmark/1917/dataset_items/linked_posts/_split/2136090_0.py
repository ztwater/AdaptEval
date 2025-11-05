>>> def chunkify(lst,n):
...     return [lst[i::n] for i in xrange(n)]
... 
>>> chunkify(range(13), 3)
[[0, 3, 6, 9, 12], [1, 4, 7, 10], [2, 5, 8, 11]]
