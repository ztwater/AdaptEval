example = {
    'id1':  {'name': 'jay','age':22,},
    'id2': {'name': 'salman','age': 52,},
    'id3': {'name':'Ranveer','age' :26,},
    'id4': {'name': 'jay', 'age': 22,},
}
for item in example:
    for value in example:
        if example[item] ==example[value]:
            if item != value:
                 key = value 
                 del example[key]
print "example",example         
