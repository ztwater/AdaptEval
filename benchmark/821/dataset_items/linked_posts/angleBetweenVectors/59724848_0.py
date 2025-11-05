@njit(cache=True, nogil=True)
def angle(vector1, vector2):
    """ Returns the angle in radians between given vectors"""
    v1_u = unit_vector(vector1)
    v2_u = unit_vector(vector2)
    minor = np.linalg.det(
        np.stack((v1_u[-2:], v2_u[-2:]))
    )
    if minor == 0:
        sign = 1
    else:
        sign = -np.sign(minor)
    dot_p = np.dot(v1_u, v2_u)
    dot_p = min(max(dot_p, -1.0), 1.0)
    return sign * np.arccos(dot_p)

@njit(cache=True, nogil=True)
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def test_angle():
    def npf(x):
        return np.array(x, dtype=float)
    assert np.isclose(angle(npf((1, 1)), npf((1,  0))),  pi / 4)
    assert np.isclose(angle(npf((1, 0)), npf((1,  1))), -pi / 4)
    assert np.isclose(angle(npf((0, 1)), npf((1,  0))),  pi / 2)
    assert np.isclose(angle(npf((1, 0)), npf((0,  1))), -pi / 2)
    assert np.isclose(angle(npf((1, 0)), npf((1,  0))),  0)
    assert np.isclose(angle(npf((1, 0)), npf((-1, 0))),  pi)
