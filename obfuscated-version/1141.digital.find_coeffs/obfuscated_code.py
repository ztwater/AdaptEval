def find_coeffs(var_0, var_1):
    var_2 = []
    for p1, p2 in zip(var_0, var_1):
        var_2.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        var_2.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])

    var_3 = numpy.matrix(var_2, dtype=numpy.float)
    var_4 = numpy.array(pb).reshape(8)

    var_5 = numpy.dot(numpy.linalg.inv(var_3.T * var_3) * var_3.T, var_4)
    return numpy.array(res).reshape(8)
