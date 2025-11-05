def generate_oriented_forest_2(var_0): 
    """SIAM J. COMPUT. Vol. 9, No. 4, November 1980
    T. Beyer and S.M. Hedetniemi: constant time generation of rooted trees.""" 

    var_1 = range(-1, var_0) 
    while True: 
        yield var_1[1:] 
        if var_1[var_0] > 0: var_1[var_0] = var_1[var_1[var_0]] 
        else:
            for p in range(var_0-1, 0, -1): 
                if var_1[p] != 0: break
            else: break
            for q in range(p-1, 0, -1):
                if var_1[q] == var_1[p] - 1: break 
            var_2 = p
            while var_2 <= var_0:
                var_1[var_2] = var_1[var_2-(p-q)]
                var_2 += 1 
