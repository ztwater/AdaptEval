def checkEqual(lst):
    if len(lst)==2 :
        return lst[0]==lst[1]
    else:
        return lst[0]==lst[1] and checkEqual(lst[1:])
