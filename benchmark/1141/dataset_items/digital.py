import numpy as np


def find_coeffs(pa, pb):
    """
    Calculate parameters for PIL perspective transform.
    Source:https://stackoverflow.com/questions/14177744/

    Args:
        pa (list): list of 4 (x, y) points to map to pb
        pb (list): list of 4 (x, y) points to be mapped from pa

    Returns:
        (np.ndarray): parameters for PIL perspective transform
    """
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])

    A = np.matrix(matrix, dtype=np.float64)
    B = np.array(pb).reshape(8)

    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)
