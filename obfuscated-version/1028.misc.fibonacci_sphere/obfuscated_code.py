import math


def fibonacci_sphere(var_0=1000):

    var_1 = []
    var_2 = math.pi * (math.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(var_0):
        var_3 = 1 - (i / float(var_0 - 1)) * 2  # y goes from 1 to -1
        var_4 = math.sqrt(1 - var_3 * var_3)  # radius at y

        var_5 = var_2 * i  # golden angle increment

        var_6 = math.cos(var_5) * var_4
        var_7 = math.sin(var_5) * var_4

        var_1.append((var_6, var_3, var_7))

    return var_1
