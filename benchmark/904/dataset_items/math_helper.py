import numpy as np

def rotation_matrix_from_vectors(reference: np.ndarray, target: np.ndarray) -> np.ndarray:
# def rotation_matrix_from_vectors(reference, target):
# def rotation_matrix_from_vectors(vec1, vec2):
# def rotation_matrix_from_vectors(v, target: np.ndarray) -> np.ndarray:
    """Find the rotation matrix that rotates a reference vector into a target vector.

    Args:
        reference (np.ndarray): Reference vector.
        target (np.ndarray): Target vector.

    Returns:
        rotation_matrix (np.ndarray): Rotation matrix that rotates the reference vector into the target vector.
    """
    # Normalize both vectors
    a, b = (reference / np.linalg.norm(reference)).reshape(3), (target / np.linalg.norm(target)).reshape(3)

    v = np.cross(a, b)
    c = np.dot(a, b)
    s = np.linalg.norm(v)

    # Construct rotation matrix
    # See https://stackoverflow.com/questions/45142959/calculate-rotation-matrix-to-align-two-vectors-in-3d-space
    kmat = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    rotation_matrix = np.eye(3) + kmat + kmat.dot(kmat) * ((1 - c) / (s ** 2))

    return rotation_matrix
