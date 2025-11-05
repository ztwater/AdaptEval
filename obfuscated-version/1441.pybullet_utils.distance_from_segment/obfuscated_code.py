def dist(var_0, var_1, var_2, var_3, var_4, var_5): # x3,y3 is the point
    var_6 = var_2-var_0
    var_7 = var_3-var_1

    var_8 = var_6*var_6 + var_7*var_7

    var_9 =  ((var_4 - var_0) * var_6 + (var_5 - var_1) * var_7) / float(var_8)

    if var_9 > 1:
        var_9 = 1
    elif var_9 < 0:
        var_9 = 0

    var_10 = var_0 + var_9 * var_6
    var_11 = var_1 + var_9 * var_7

    var_12 = var_10 - var_4
    var_13 = var_11 - var_5

    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance

    var_14 = (var_12*var_12 + var_13*var_13)**.5

    return var_14
