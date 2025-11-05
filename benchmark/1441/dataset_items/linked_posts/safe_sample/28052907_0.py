>>> from collections_extended import setlist
>>> sl = setlist('abracadabra')
>>> sl
setlist(('a', 'b', 'r', 'c', 'd'))
>>> sl[3]
'c'
>>> sl[-1]
'd'
>>> 'r' in sl  # testing for inclusion is fast
True
>>> sl.index('d')  # so is finding the index of an element
4
>>> sl.insert(1, 'd')  # inserting an element already in raises a ValueError
ValueError
>>> sl.index('d')
4
