def chunks(iterable,n):
    """assumes n is an integer>0
    """
    iterable=iter(iterable)
    while True:
        result=[]
        for i in range(n):
            try:
                a=next(iterable)
            except StopIteration:
                break
            else:
                result.append(a)
        if result:
            yield result
        else:
            break

g1=(i*i for i in range(10))
g2=chunks(g1,3)
print g2
'<generator object chunks at 0x0337B9B8>'
print list(g2)
'[[0, 1, 4], [9, 16, 25], [36, 49, 64], [81]]'
