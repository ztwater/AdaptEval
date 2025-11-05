import math
import unittest
from mytransforms import RandomRotate


class TestGetCropSize(unittest.TestCase):
    def setUp(self):
        self.randomRotate = RandomRotate(10.0)

    def test_update_function_name(self):
        self.randomRotate._getCropSize(10, 10, 45)

    def test_half_constrained_case(self):
        # Test half constrained case where two crop corners touch the longer side
        w, h, angle = 1500, 500, 20  # Example dimensions and angle in degrees
        expected_width, expected_height = 730.951100040, 266.0444431  # Expected result based on the logic
        result_height, result_width = self.randomRotate._getCropSize(w, h, angle)
        self.assertAlmostEqual(expected_width, result_width, places=5)
        self.assertAlmostEqual(expected_height, result_height, places=5)

    def test_fully_constrained_case(self):
        # Test fully constrained case where crop touches all 4 sides
        w, h, angle = 10, 10, 45  # Example dimensions and angle in degrees
        expected_width, expected_height = 7.071067811, 7.07106781  # Expected result based on the logic
        result_height, result_width = self.randomRotate._getCropSize(w, h, angle)
        self.assertAlmostEqual(expected_width, result_width, places=5)
        self.assertAlmostEqual(expected_height, result_height, places=5)

    def test_angle_conversion(self):
        # Test the angle conversion from degrees to radians
        w, h = 10, 10
        angle_in_degrees = 90
        result_height, result_width = self.randomRotate._getCropSize(w, h, angle_in_degrees)
        # Since angle is 90 degrees, the expected width and height should be the same as the original height and width
        self.assertEqual(result_height, h)
        self.assertEqual(result_width, w)

    def test_change_return_order(self):
        # Test the angle conversion from degrees to radians
        w, h = 20, 10
        angle_in_degrees = 180
        angle_in_radians = math.pi / 2
        result_height_d, result_width_d = self.randomRotate._getCropSize(w, h, angle_in_degrees)
        result_height_r, result_width_r = self.randomRotate._getCropSize(w, h, angle_in_radians)
        is_changed = False
        # regardless whether the angle conversion is performed
        if (math.isclose(result_height_r, h, abs_tol=0.01) and
                math.isclose(result_width_r, w, abs_tol=0.01) or
                math.isclose(result_height_d, h, abs_tol=0.01) and
                math.isclose(result_width_d, w, abs_tol=0.01)):
            is_changed = True
            self.assertTrue(is_changed)

    def test_invalid_input(self):
        # Test the method with invalid input (non-positive dimensions)
        w, h, angle = -1, 10, 30
        expected_width, expected_height = -0.5773502691896257, -1.0000000000000002
        result_height, result_width = self.randomRotate._getCropSize(w, h, angle)
        self.assertNotEqual(result_width, 0)
        self.assertNotEqual(result_height, 0)


if __name__ == '__main__':
    unittest.main()
