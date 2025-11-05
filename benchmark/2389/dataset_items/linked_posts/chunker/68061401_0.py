def chunker(it,size):
    rv = [] 
    for i,el in enumerate(it,1) :   
        rv.append(el)
        if i % size == 0 : 
            yield rv
            rv = []
    if rv : yield rv        
