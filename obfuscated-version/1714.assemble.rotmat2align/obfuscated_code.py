def rotation_matrix_from_vectors(var_0, var_1):
    """ Find the rotation matrix that aligns vec1 to vec2
    :param vec1: A 3d "source" vector
    :param vec2: A 3d "destination" vector
    :return mat: A transform matrix (3x3) which when applied to vec1, aligns it with vec2.
    """
    a, b = (vec1 / np.linalg.norm(vec1)).reshape(3), (vec2 / np.linalg.norm(vec2)).reshape(3)
    var_2 = np.cross(a, b)
    var_3 = np.dot(a, b)
    var_4 = np.linalg.norm(var_2)
    var_5 = np.array([[0, -var_2[2], var_2[1]], [var_2[2], 0, -var_2[0]], [-var_2[1], var_2[0], 0]])
    var_6 = np.eye(3) + var_5 + var_5.dot(var_5) * ((1 - var_3) / (var_4 ** 2))
    return var_6
