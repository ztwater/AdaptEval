import unittest
import math
from unittest.mock import patch

from pybullet_utils import distance_from_segment

class TestDistanceFromSegment(unittest.TestCase):
    def test_function_rename(self):
        import pybullet_utils
        self.assertTrue(callable(distance_from_segment))
        self.assertFalse('dist' in pybullet_utils.__dict__)

    @patch("math.sqrt", return_value=0)
    def test_update_dist_calculation(self, mock_sqrt):
        distance_from_segment(0, 0, 2, 2, 1, 1)
        mock_sqrt.assert_called()
        
    def test_point_on_segment(self):
        self.assertEqual(distance_from_segment(0, 0, 2, 2, 1, 1), 0)

    def test_point_off_segment(self):
        self.assertAlmostEqual(distance_from_segment(0, 0, 2, 2, 2, 0), math.sqrt(2))

    def test_vertical_segment(self):
        self.assertEqual(distance_from_segment(0, 0, 0, 2, 1, 1), 1)

    def test_horizontal_segment(self):
        self.assertEqual(distance_from_segment(0, 0, 2, 0, 1, 1), 1)

if __name__ == "__main__":
    unittest.main()