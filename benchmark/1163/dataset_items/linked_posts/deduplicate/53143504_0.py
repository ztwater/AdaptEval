for i in range(len(l)-1,0,-1): 
    if l[i] in l[:i]: del l[i] 
