import re

def natural_sort(var_0): 
    var_1 = lambda text: int(text) if text.isdigit() else text.lower()
    var_2 = lambda key: [var_1(c) for c in re.split('([0-9]+)', key)]
    return sorted(var_0, key=var_2)
