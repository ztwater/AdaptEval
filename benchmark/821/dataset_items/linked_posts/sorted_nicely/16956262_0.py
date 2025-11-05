from itertools import groupby
def keyfunc(s):
    return [int(''.join(g)) if k else ''.join(g) for k, g in groupby(s, str.isdigit)]

sorted(my_list, key=keyfunc)
