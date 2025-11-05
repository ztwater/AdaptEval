groupby(iterable, (lambda x,y: (lambda z: x.next()/y))(count(),100))
