mylist = [x for i,x in enumerate(mylist) if x not in mylist[i+1:]]
