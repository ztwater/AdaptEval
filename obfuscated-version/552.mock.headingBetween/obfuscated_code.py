import math, numpy as np

def get_bearing(var_0,var_1,var_2,var_3):
    var_4 = var_3 - var_1;
    var_5 = math.sin(var_4) * math.cos(var_2);
    var_6 = math.cos(var_0)*math.sin(var_2) - math.sin(var_0)*math.cos(var_2)*math.cos(var_4);
    var_7 = np.rad2deg(math.atan2(var_5, var_6));
    if var_7 < 0: var_7+= 360
    return var_7
