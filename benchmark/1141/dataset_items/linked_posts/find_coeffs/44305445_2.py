def find_rotation_coeffs(theta, x0, y0):
    ct = cos(theta)
    st = sin(theta)
    return np.array([ct, -st, x0*(1-ct) + y0*st, st, ct, y0*(1-ct)-x0*st,0,0])
