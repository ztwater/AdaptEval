def rotate(var_0, var_1, var_2):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = var_0
    px, py = var_1

    var_3 = ox + math.cos(var_2) * (px - ox) - math.sin(var_2) * (py - oy)
    var_4 = oy + math.sin(var_2) * (px - ox) + math.cos(var_2) * (py - oy)
    return var_3, var_4
