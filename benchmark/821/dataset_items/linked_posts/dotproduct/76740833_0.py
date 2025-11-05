def angle(a, b, c=None):
    """ This function computes angle between vector A and vector B when C is None
        and the angle between AC and CB, when C is a vector as well.
        All vectors must be two dimensional.
    """
    if c is None:
        angles = np.arctan2([a[1], b[1]], [a[0], b[0]]])
    else:
        angles = np.arctan2([a[1]-c[1], b[1]-c[1]], [a[0]-c[0], b[0]-c[0]])
    return np.degrees(angles[1] - angles[0])
