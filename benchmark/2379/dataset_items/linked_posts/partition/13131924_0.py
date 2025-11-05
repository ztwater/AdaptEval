def partition(lista,bins):
    if len(lista)==1 or bins==1:
        yield [lista]
    elif len(lista)>1 and bins>1:
        for i in range(1,len(lista)):
            for part in partition(lista[i:],bins-1):
                if len([lista[:i]]+part)==bins:
                    yield [lista[:i]]+part

for i in partition(range(1,5),1): 
    print i
#[[1, 2, 3, 4]]

for i in partition(range(1,5),2): 
    print i
#[[1], [2, 3, 4]]
#[[1, 2], [3, 4]]
#[[1, 2, 3], [4]]

for i in partition(range(1,5),3):
    print i
#[[1], [2], [3, 4]]
#[[1], [2, 3], [4]]
#[[1, 2], [3], [4]] 

for i in partition(range(1,5),4):
    print i
#[[1], [2], [3], [4]]
