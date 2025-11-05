import unittest
import numpy as np
from loading import LoadBuildingAnnotations
import inspect

class TestPolygonArea(unittest.TestCase):
    def setUp(self):
        self.calculator = LoadBuildingAnnotations()

    def test_simple_polygon(self):
        # Test with a simple square polygon
        square = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
        expected_area = 1.0  # Area of the square
        calculated_area = self.calculator._polygon_area(square)
        self.assertAlmostEqual(expected_area, calculated_area, places=5)

    def test_rectangle_polygon(self):
        # Test with a rectangle polygon
        rectangle = np.array([[0, 0], [2, 0], [2, 1], [0, 1]])
        expected_area = 2.0  # Area of the rectangle
        calculated_area = self.calculator._polygon_area(rectangle)
        self.assertAlmostEqual(expected_area, calculated_area, places=5)

    def test_large_coordinates(self):
        # Test with large coordinates to check for numerical stability
        large_polygon = np.array([[1000000, 1000000], [1000001, 1000000], [1000001, 1000001], [1000000, 1000001]])
        expected_area = 1.0  # Area of the large square
        calculated_area = self.calculator._polygon_area(large_polygon)
        self.assertAlmostEqual(expected_area, calculated_area, places=5)

    def test_rename_method(self):
        self.assertIsNotNone(getattr(LoadBuildingAnnotations, '_polygon_area'))

    def test_add_local_parameter(self):
        signature = inspect.signature(self.calculator._polygon_area)
        # Check if the method has the correct annotations
        parameters = signature.parameters
        self.assertEqual("poly", list(parameters.keys())[0])


if __name__ == '__main__':
    unittest.main()
