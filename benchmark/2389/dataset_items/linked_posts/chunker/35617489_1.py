for k,v in groupby(bigdata, (lambda x,y: (lambda z: x.next()/y))(count(),100))):
    cursor.executemany(sql, v)
