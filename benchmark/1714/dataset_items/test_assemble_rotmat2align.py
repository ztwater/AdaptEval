import unittest
import numpy as np

from assemble import rotmat2align

class TestRotmat2align(unittest.TestCase):

    def setUp(self):
        # Set up some initial vectors for testing
        self.vec1 = np.array([1, 0, 0])
        self.vec2 = np.array([0, 1, 0])
        self.vec3 = np.array([0, 0, 1])
        self.vec4 = np.array([-1, 0, 0])  # Opposite direction
        self.vec5 = np.array([0, 1, 1])   # Non-unit vector

    def test_basic_rotation(self):
        # Test the basic functionality of the rotation matrix
        expected_rotation_matrix = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
        rotation_matrix = rotmat2align(self.vec1, self.vec2)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_rotation_matrix)

    def test_non_unit_vector(self):
        # Test the case where the second vector is not a unit vector
        normalized_vec2 = self.vec5 / np.linalg.norm(self.vec5)
        expected_rotation_matrix = rotmat2align(self.vec1, normalized_vec2)
        rotation_matrix = rotmat2align(self.vec1, self.vec5)
        np.testing.assert_array_almost_equal(rotation_matrix, expected_rotation_matrix)

    def test_invalid_input(self):
        # Test the function with invalid inputs (e.g., not 3D vectors)
        with self.assertRaises(ValueError):
            rotmat2align(np.array([1, 0]), np.array([0, 1]))

    def test_rotation_effect(self):
        # Test the effect of the rotation on a vector
        rotation_matrix = rotmat2align(self.vec1, self.vec3)
        rotated_vec1 = np.dot(rotation_matrix, self.vec1)
        np.testing.assert_array_almost_equal(rotated_vec1, self.vec3)

    def test_rename_function(self):
        import assemble
        self.assertTrue(callable(rotmat2align))
        self.assertNotIn('rotation_matrix_from_vectors', assemble.__dict__)

if __name__ == '__main__':
    unittest.main()