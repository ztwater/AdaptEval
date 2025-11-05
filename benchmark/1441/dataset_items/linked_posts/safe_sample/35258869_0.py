>>> from boltons.setutils import IndexedSet
>>> x = IndexedSet(list(range(4)) + list(range(8)))
>>> x
IndexedSet([0, 1, 2, 3, 4, 5, 6, 7])
>>> x - set(range(2))
IndexedSet([2, 3, 4, 5, 6, 7])
>>> x[-1]
7
>>> fcr = IndexedSet('freecreditreport.com')
>>> ''.join(fcr[:fcr.index('.')])
'frecditpo'
