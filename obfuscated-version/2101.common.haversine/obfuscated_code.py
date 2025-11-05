def haversine(var_0, var_1, var_2, var_3):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    var_0, var_1, var_2, var_3 = map(radians, [var_0, var_1, var_2, var_3])

    # haversine formula 
    var_4 = var_2 - var_0 
    var_5 = var_3 - var_1 
    var_6 = sin(var_5/2)**2 + cos(var_1) * cos(var_3) * sin(var_4/2)**2
    var_7 = 2 * asin(sqrt(var_6)) 
    var_8 = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return var_7 * var_8
