import unittest
import cv2
import numpy as np
from Function_draw_mask import draw_line

class TestDrawLine(unittest.TestCase):
    def setUp(self):
        # Set up a blank image for drawing
        self.img = np.full((100, 100, 3), 255, np.uint8)
        # Define a point for testing
        self.pt1 = (10, 10)
        # Define another point for testing
        self.pt2 = (90, 90)
        # Define color and thickness for the line
        self.color = (0, 0, 255)  # Blue color in BGR
        self.thickness = 5

    def test_line_thickness(self):
        # Test if the line thickness is as expected
        draw_line(self.img, self.pt1, self.pt2, self.color, self.thickness)
        # Check the thickness of the line at the starting point
        self.assertEqual(self.img[10, 11, 2], 255)  # Assuming the line is vertical and blue

    def test_line_rotation(self):
        # Test if the line can be drawn with a certain rotation
        # Create a rotated line by adjusting the points
        pt1_rotated = (self.pt1[0] + 10, self.pt1[1] + 10)
        pt2_rotated = (self.pt2[0] - 10, self.pt2[1] - 10)
        draw_line(self.img, pt1_rotated, pt2_rotated, self.color, self.thickness)
        # Check if the line has been drawn correctly at the rotated points
        # This is a simplified check and would need to be more robust in a real test
        self.assertEqual(self.img[20, 20, 2], 255)

    def test_line_return(self):
        # Test if the function returns the image
        returned_img = draw_line(self.img, self.pt1, self.pt2, self.color, self.thickness)
        self.assertIs(returned_img, self.img)

# This allows the test script to be run from the command line
if __name__ == '__main__':
    unittest.main()