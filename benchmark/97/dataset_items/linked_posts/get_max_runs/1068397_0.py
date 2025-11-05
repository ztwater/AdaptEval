>>> from numpy import array, arange
>>> b = array([0,0,0,1,1,1,0,0,0,1,1,1,1,0,0], dtype=bool)
>>> sw = (b[:-1] ^ b[1:]); print sw
[False False  True False False  True False False  True False False False
  True False]
>>> isw = arange(len(sw))[sw]; print isw
[ 2  5  8 12]
>>> lens = isw[1::2] - isw[::2]; print lens
[3 4]
