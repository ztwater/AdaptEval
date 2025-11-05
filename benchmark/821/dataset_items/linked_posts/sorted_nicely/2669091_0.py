>>> a = set(['booklet', '4 sheets', '48 sheets', '12 sheets'])
>>> def ke(s):
    i, sp, _ = s.partition(' ')
    if i.isnumeric():
        return int(i)
    return float('inf')

>>> sorted(a, key=ke)
['4 sheets', '12 sheets', '48 sheets', 'booklet']
