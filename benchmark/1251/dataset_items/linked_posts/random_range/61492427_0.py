import random

sourcelist=[]
resultlist=[]

for x in range(100):
    sourcelist.append(x)

for y in sourcelist:
    resultlist.insert(random.randint(0,len(resultlist)),y)

print (resultlist)
