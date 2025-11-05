from itertools import islice

def split_every(var_0, var_1):
    var_2 = iter(var_1)
    var_3 = list(islice(var_2, var_0))
    while var_3:
        yield var_3
        var_3 = list(islice(var_2, var_0))
