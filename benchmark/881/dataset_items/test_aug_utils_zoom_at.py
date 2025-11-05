import unittest
from unittest.mock import patch
from PIL import Image
from io import BytesIO

from aug_utils import zoom_at

class TestZoomAt(unittest.TestCase):
    def setUp(self):
        # Load a test image for use in the tests
        self.test_image = Image.open('./function.png')

    def test_zoom_at_basic(self):
        zoom_factor = 2.0
        zoomed_image = zoom_at(self.test_image, 100, 100, zoom_factor)
        self.assertEqual(zoomed_image.size, self.test_image.size)

    def test_zoom_at_center(self):
        w, h = self.test_image.size
        zoom_factor = 1.5
        zoomed_image = zoom_at(self.test_image, w // 2, h // 2, zoom_factor)
        self.assertEqual(zoomed_image.size, self.test_image.size)

    def test_zoom_at_edge(self):
        zoom_factor = 1.5
        zoomed_image = zoom_at(self.test_image, 0, 0, zoom_factor)
        self.assertEqual(zoomed_image.size, self.test_image.size)

    # return annotation
    def test_add_type_annotations(self):
        annotations = zoom_at.__annotations__
        # Check if the return annotation exists and is 'str'
        self.assertIn('return', annotations)
        self.assertEqual(annotations['return'], Image.Image)
        self.assertEqual(annotations['img'], Image.Image)
        self.assertEqual(annotations['x'], int)
        self.assertEqual(annotations['y'], int)
        self.assertEqual(annotations['zoom'], float)

    @patch("builtins.int", return_value=0)
    def test_add_type_conversion(self, mock_int):
        zoomed_image = zoom_at(self.test_image, 100, 100, 2)
        self.assertEqual(mock_int.call_count, 8)

    def tearDown(self):
        # Clean up after tests
        self.test_image.close()

if __name__ == '__main__':
    unittest.main()
