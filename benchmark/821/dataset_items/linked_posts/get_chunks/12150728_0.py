def chunker(iterable, chunksize):
    for i,c in enumerate(iterable[::chunksize]):
        yield iterable[i*chunksize:(i+1)*chunksize]

>>> for chunk in chunker(range(0,100), 10):
...     print list(chunk)
... 
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
[20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
... etc ...
