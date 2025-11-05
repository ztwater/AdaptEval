def update(key,value,dictionary):
    if key in dictionary.keys():
        dictionary[key] = value
        return
    dic_aux = []
    for val_aux in dictionary.values():
        if isinstance(val_aux,dict):
            dic_aux.append(val_aux)
    for i in dic_aux:
        update(key,value,i)
    for [key2,val_aux2] in dictionary.items():
        if isinstance(val_aux2,dict):
            dictionary[key2] = val_aux2

dictionary1={'level1':{'level2':{'levelA':0,'levelB':1}}}
update('levelB',10,dictionary1)
print(dictionary1)

#output: {'level1': {'level2': {'levelA': 0, 'levelB': 10}}}
