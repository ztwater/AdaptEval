vec1 = [2, 3, 2.5]
vec2 = [-3, 1, -3.4]

mat = rotation_matrix_from_vectors(vec1, vec2)
vec1_rot = mat.dot(vec1)
assert np.allclose(vec1_rot/np.linalg.norm(vec1_rot), vec2/np.linalg.norm(vec2))
