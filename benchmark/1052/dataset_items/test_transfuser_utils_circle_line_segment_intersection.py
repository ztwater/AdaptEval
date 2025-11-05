import unittest
from transfuser_utils import circle_line_segment_intersection


class TestCircleLineSegmentIntersection(unittest.TestCase):

    def test_zero_length_segment(self):
        """Tests if the function handles zero-length line segments."""
        center = (0, 0)
        radius = 1
        pt1 = (0, 0)
        pt2 = (0, 0)
        with self.assertRaises(ZeroDivisionError):
            circle_line_segment_intersection(center, radius, pt1, pt2)

    def test_intersection_on_segment(self):
        """Tests if the function finds intersections on the line segment."""
        center = (0, 0)
        radius = 1
        pt1 = (-1, 0)
        pt2 = (1, 0)
        intersections = circle_line_segment_intersection(center, radius, pt1, pt2)
        self.assertEqual(len(intersections), 2)
        self.assertIn((-1.0, 0.0), intersections)
        self.assertIn((1.0, 0.0), intersections)

    def test_intersection_outside_segment(self):
        """Tests if the function excludes intersections outside the segment (full_line=False)."""
        center = (0, 0)
        radius = 1
        pt1 = (-1.14, 0)
        pt2 = (0.9, 0)
        intersections = circle_line_segment_intersection(center, radius, pt1, pt2, full_line=False)
        self.assertEqual(len(intersections), 1)
        self.assertIn((-1.0, 0), intersections)

    def test_tangent_case(self):
        """Tests if the function handles tangent cases correctly."""
        center = (0, 0)
        radius = 1
        pt1 = (-1, 1)
        pt2 = (1, 1)
        intersections = circle_line_segment_intersection(center, radius, pt1, pt2)
        self.assertEqual(len(intersections), 1)
        self.assertIn((0, 1), intersections)


if __name__ == "__main__":
    unittest.main()