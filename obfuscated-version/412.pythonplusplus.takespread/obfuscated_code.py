from math import ceil

def takespread(var_0, var_1):
    var_2 = float(len(var_0))
    for i in range(var_1):
        yield var_0[int(ceil(i * var_2 / var_1))]
