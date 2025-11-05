import re
natsort = lambda s: [int(t) if t.isdigit() else t.lower() for t in re.split('(\d+)', s)]
L = ["a1", "a10", "a11", "a2", "a22", "a3"]   
print(sorted(L, key=natsort))  
# ['a1', 'a2', 'a3', 'a10', 'a11', 'a22'] 
