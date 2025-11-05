def row_col_from_condensed_index(var_0,var_1):
    var_2 = 1 - (2 * var_0) 
    var_3 = (-var_2 - math.sqrt(var_2 ** 2 - 8 * var_1)) // 2
    var_4 = var_1 + var_3 * (var_2 + var_3 + 2) // 2 + 1
    return (var_3,var_4)  
