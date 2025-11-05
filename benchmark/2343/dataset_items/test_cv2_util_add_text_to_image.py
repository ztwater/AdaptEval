import unittest
import numpy as np
import cv2
from typing import Tuple, Optional
from cv2_util import add_text_to_image
import inspect

class TestAddTextToImage(unittest.TestCase):
    def setUp(self):
        self.image = np.ones((100, 300, 3), np.uint8) * 255  # 白色背景
        self.label = "Test"

    def test_replace_optional_annotations(self):
        annotations = add_text_to_image.__annotations__
        self.assertIn('Optional', str(annotations['bg_color_rgb']))
        self.assertIn('Optional', str(annotations['outline_color_rgb']))

    def test_update_tuple_annotations(self):
        annotations = add_text_to_image.__annotations__
        self.assertNotEqual(annotations['top_left_xy'], tuple)
        self.assertNotEqual(annotations['font_color_rgb'], tuple)
        self.assertEqual(annotations['top_left_xy'], Tuple)
        self.assertEqual(annotations['font_color_rgb'], Tuple)
        self.assertEqual(annotations['bg_color_rgb'], Optional[Tuple])
        self.assertEqual(annotations['outline_color_rgb'], Optional[Tuple])

    def test_optional_bg_color(self):
        result = add_text_to_image(self.image, self.label, bg_color_rgb=None)
        self.assertIsNotNone(result)
        self.assertTrue(np.array_equal(result, self.image))

    def test_optional_outline_color(self):
        result = add_text_to_image(self.image, self.label, outline_color_rgb=None)
        self.assertIsNotNone(result)
        self.assertTrue(np.array_equal(result, self.image))
    
    def test_text_with_tuple_type_annotations(self):
        image_copy = self.image.copy()  # 使用图像的副本进行测试
        result = add_text_to_image(image_copy, self.label, top_left_xy=(10, 20), font_color_rgb=(255, 0, 0))
        self.assertIsNotNone(result)
        self.assertFalse(np.array_equal(result, self.image))  # 检查图像是否已更改
        self.assertTrue(np.any(result != self.image))  # 确保文本已被添加


if __name__ == "__main__":
    unittest.main()
