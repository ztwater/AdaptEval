a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CHUNK = 4
[a[i*CHUNK:(i+1)*CHUNK] for i in xrange((len(a) + CHUNK - 1) / CHUNK )]
