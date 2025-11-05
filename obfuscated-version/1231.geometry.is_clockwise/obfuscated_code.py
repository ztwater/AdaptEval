def is_clockwise(var_0):
    # points is your list (or array) of 2d points.
    assert len(var_0) > 0
    var_1 = 0.0
    for p1, p2 in zip(var_0, var_0[1:] + [var_0[0]]):
        var_1 += (p2[0] - p1[0]) * (p2[1] + p1[1])
    return var_1 > 0.0
