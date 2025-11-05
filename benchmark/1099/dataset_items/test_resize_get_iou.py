import unittest
from resize import get_iou


class TestGetIou(unittest.TestCase):
    def test_iou_normal_case(self):
        bb1 = {'x1': 0, 'x2': 2, 'y1': 0, 'y2': 2}
        bb2 = {'x1': 1, 'x2': 3, 'y1': 1, 'y2': 3}
        self.assertAlmostEqual(get_iou(bb1, bb2), 1/7)

    def test_iou_no_overlap(self):
        bb1 = {'x1': 0, 'x2': 1, 'y1': 0, 'y2': 1}
        bb2 = {'x1': 2, 'x2': 3, 'y1': 2, 'y2': 3}
        self.assertEqual(get_iou(bb1, bb2), 0.0)

    def test_iou_complete_overlap(self):
        bb1 = {'x1': 0, 'x2': 2, 'y1': 0, 'y2': 2}
        bb2 = {'x1': 0, 'x2': 2, 'y1': 0, 'y2': 2}
        self.assertEqual(get_iou(bb1, bb2), 1.0)

    def test_iou_zero_area(self):
        bb1 = {'x1': 0, 'x2': 0, 'y1': 0, 'y2': 0}
        bb2 = {'x1': 0, 'x2': 0, 'y1': 0, 'y2': 0}
        self.assertEqual(get_iou(bb1, bb2), 1.0)

    def test_iou_invalid(self):
        bb1 = {'x1': 1, 'x2': 0, 'y1': 0, 'y2': 2}
        bb2 = {'x1': 0, 'x2': 2, 'y1': 0, 'y2': 2}
        with self.assertRaises(AssertionError):
            get_iou(bb1, bb2)

if __name__ == '__main__':
    unittest.main()
