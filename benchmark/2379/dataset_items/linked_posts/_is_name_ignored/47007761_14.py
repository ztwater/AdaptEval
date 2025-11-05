def foo(*args):
    r = [x for x in args if x > 9000]
    if not r:
        return 'No number over 9000!' 
    
    return r
