list(map(list, zip(*[iter(lst)]*n))) + ([rest] if (rest:=lst[len(lst)//n*n : ]) else [])
