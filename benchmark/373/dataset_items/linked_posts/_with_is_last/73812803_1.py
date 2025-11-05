d = {'a': (1,2,3), 'b': (4,5,6), 'c': (7,8,9)}

for (k,v), is_first, is_last in metait(d.items()):
    print(f'{k}: {v}  {is_first} {is_last}')
