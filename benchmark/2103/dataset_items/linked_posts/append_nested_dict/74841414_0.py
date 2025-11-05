def m3(a,b):
    if not isinstance(a,dict) and not isinstance(b,dict):return b
    for k in b:
        if k in a :
            a[k] = m3(a[k], b[k])
        else: a[k] = b[k] 
    return a       
            
d1 = {1:{"a":"A"}, 2:{"b":"B"}}

d2 = {2:{"c":"C"}, 3:{"d":"D"}}
d3 = {1:{"a":{1}}, 2:{"b":{2}}}

d4 = {2:{"c":{222}}, 3:{"d":{3}}}
d5 = {'employee':{'dev1': 'Roy'}}
d6 = {'employee':{'dev2': 'Biswas'}}

print(m3(d1,d2))

print(m3(d3,d4))
print(m3(d5,d6))

"""
Output :
{1: {'a': 'A'}, 2: {'b': 'B', 'c': 'C'}, 3: {'d': 'D'}}
{1: {'a': {1}}, 2: {'b': {2}, 'c': {222}}, 3: {'d': {3}}}
{'employee': {'dev1': 'Roy', 'dev2': 'Biswas'}}

"""
