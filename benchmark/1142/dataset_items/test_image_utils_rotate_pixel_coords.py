import unittest
from math import cos, sin, pi
from image_utils import rotate_pixel_coords
from typing import Tuple

class TestRotatePixelCoords(unittest.TestCase):
    def test_rotation_0_degrees(self):
        # No change expected with 0 degree rotation.
        origin = (5, 5)
        point = (10, 10)
        expected = (10, 10)
        self.assertEqual(rotate_pixel_coords(origin, point, 0), expected)

    def test_rotation_90_degrees(self):
        # Point should move to the left of the origin.
        origin = (5, 5)
        point = (5, 10)
        expected = (0, 5)
        self.assertEqual(rotate_pixel_coords(origin, point, 90 * pi / 180), expected)

    def test_rotation_180_degrees(self):
        # Point should move to the opposite side of the origin.
        origin = (5, 5)
        point = (10, 10)
        expected = (0, 0)
        self.assertEqual(rotate_pixel_coords(origin, point, 180 * pi / 180), expected)

    def test_rotation_45_degrees(self):
        # General case for a 45 degree rotation.
        origin = (0, 0)
        point = (0, 2)
        angle = 45 / 360 * 2 * pi  # Convert 45 degrees to radians
        expected_x = -1
        expected_y = 1
        expected = (expected_x, expected_y)
        self.assertEqual(rotate_pixel_coords(origin, point, angle), expected)

    def test_add_type_annotations(self):
        annotations = rotate_pixel_coords.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], Tuple[int,int])
        self.assertEqual(annotations['origin'], Tuple[int,int])
        self.assertEqual(annotations['point'], Tuple[int,int])
        self.assertEqual(annotations['angle'], float)

    def test_rename_function(self):
        from image_utils import rotate_pixel_coords
        self.assertTrue(callable(rotate_pixel_coords))

    def test_add_type_conversion(self):
        origin = (0, 0)
        point = (0, 2)
        angle = 45 / 360 * 2 * pi  # Convert 45 degrees to radians
        result = rotate_pixel_coords(origin, point, angle)
        self.assertNotAlmostEqual(result[0], -1.4142, delta=0.001)
        self.assertNotAlmostEqual(result[1], 1.4142, delta=0.001)

if __name__ == '__main__':
    unittest.main()