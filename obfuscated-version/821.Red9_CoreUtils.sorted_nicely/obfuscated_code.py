import re 

def sorted_nicely( var_0 ): 
    """ Sort the given iterable in the way that humans expect.""" 
    var_1 = lambda text: int(text) if text.isdigit() else text 
    var_2 = lambda key: [ var_1(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(var_0, key = var_2)
