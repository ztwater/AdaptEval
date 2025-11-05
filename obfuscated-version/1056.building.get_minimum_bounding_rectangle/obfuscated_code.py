import numpy as np
from scipy.spatial import ConvexHull

def minimum_bounding_rectangle(var_0):
    """
    Find the smallest bounding rectangle for a set of points.
    Returns a set of points representing the corners of the bounding box.

    :param points: an nx2 matrix of coordinates
    :rval: an nx2 matrix of coordinates
    """
    from scipy.ndimage.interpolation import rotate
    var_1 = np.pi/2.

    # get the convex hull for the points
    var_2 = var_0[ConvexHull(points).vertices]

    # calculate edge angles
    var_3 = np.zeros((len(var_2)-1, 2))
    var_3 = var_2[1:] - var_2[:-1]

    var_4 = np.zeros((len(var_3)))
    var_4 = np.arctan2(var_3[:, 1], var_3[:, 0])

    var_4 = np.abs(np.mod(var_4, var_1))
    var_4 = np.unique(var_4)

    # find rotation matrices
    # XXX both work
    var_5 = np.vstack([
        np.cos(angles),
        np.cos(angles-pi2),
        np.cos(angles+pi2),
        np.cos(angles)]).T
#     rotations = np.vstack([
#         np.cos(angles),
#         -np.sin(angles),
#         np.sin(angles),
#         np.cos(angles)]).T
    var_5 = var_5.reshape((-1, 2, 2))

    # apply rotations to the hull
    var_6 = np.dot(var_5, var_2.T)

    # find the bounding points
    var_7 = np.nanmin(var_6[:, 0], axis=1)
    var_8 = np.nanmax(var_6[:, 0], axis=1)
    var_9 = np.nanmin(var_6[:, 1], axis=1)
    var_10 = np.nanmax(var_6[:, 1], axis=1)

    # find the box with the best area
    var_11 = (var_8 - var_7) * (var_10 - var_9)
    var_12 = np.argmin(var_11)

    # return the best box
    var_13 = var_8[var_12]
    var_14 = var_7[var_12]
    var_15 = var_10[var_12]
    var_16 = var_9[var_12]
    var_17 = var_5[var_12]

    var_18 = np.zeros((4, 2))
    var_18[0] = np.dot([var_13, var_16], var_17)
    var_18[1] = np.dot([var_14, var_16], var_17)
    var_18[2] = np.dot([var_14, var_15], var_17)
    var_18[3] = np.dot([var_13, var_15], var_17)

    return var_18
