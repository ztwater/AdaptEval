def updateDict(dict1,dict2):
    keys1 = list(dict1.keys())
    keys2= list(dict2.keys())
    keys2 = [x for x in keys2 if x in keys1]
    for x in keys2:
        if (x in keys1) & (type(dict1[x]) is dict) & (type(dict2[x]) is dict):
            updateDict(dict1[x],dict2[x])
        else:
            dict1.update({x:dict2[x]})
    return(dict1)
