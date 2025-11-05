def from_roman(var_0):
    var_1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    var_2 = 0
    for i,c in enumerate(var_0):
        if (i+1) == len(var_0) or var_1[c] >= var_1[var_0[i+1]]:
            var_2 += var_1[c]
        else:
            var_2 -= var_1[c]
    return var_2
