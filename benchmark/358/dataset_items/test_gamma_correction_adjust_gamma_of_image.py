import inspect
import unittest
import numpy as np
import cv2
import inspect
import re

from gamma_correction import adjust_gamma_of_image


class TestAdjustGammaOfImage(unittest.TestCase):

    def setUp(self):
        # Set up a simple test image
        self.image = np.array([[0, 128, 255]], dtype=np.uint8)

    def test_adjust_gamma_default(self):
        # Test the function with default gamma
        result = adjust_gamma_of_image(self.image)
        expected = self.image  # No change since default gamma is 1.0
        np.testing.assert_array_equal(result, expected)

    def test_adjust_gamma_inverted(self):
        # Test the function with gamma = 2.0 (should darken the image)
        result = adjust_gamma_of_image(self.image, gamma=2.0)
        expected = cv2.LUT(self.image,
                           np.array([((i / 255.0) ** 0.5) * 255 for i in np.arange(0, 256)]).astype("uint8"))
        np.testing.assert_array_equal(result, expected)

    def test_output_dtype(self):
        # Test that the output image dtype is uint8
        result = adjust_gamma_of_image(self.image, gamma=2.0)
        self.assertEqual(result.dtype, np.uint8)

    def test_remove_image_dtype(self):
        image = np.array([[0, 128, 255]], dtype=np.float32)
        with self.assertRaises(cv2.error):
            result = adjust_gamma_of_image(image)

    def test_move_astype_conversion(self):
        source = inspect.getsource(adjust_gamma_of_image)
        matched_astype_after_creation = re.search(r'np\.array\(.*\)\.astype\([\'|"]uint8[\'|"]\)', source, re.DOTALL)
        self.assertIsNotNone(matched_astype_after_creation)


if __name__ == '__main__':
    unittest.main()
