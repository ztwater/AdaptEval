import unittest
import numpy as np
import cv2

from renderer import rounded_rectangle

def show_image(image):
    if image is not None:
        # Display the image in a window named 'window title'
        cv2.imshow('window title', image)

        # Wait for a key press and then close the window
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def correct_draw(src, p1, p2, p3, p4, corner_radius, color=255, thickness=1, line_type=cv2.LINE_AA):
    if thickness < 0:
        # big rect
        top_left_main_rect = (int(p1[0] + corner_radius), int(p1[1]))
        bottom_right_main_rect = (int(p3[0] - corner_radius), int(p3[1]))

        top_left_rect_left = (p1[0], p1[1] + corner_radius)
        bottom_right_rect_left = (p4[0] + corner_radius, p4[1] - corner_radius)

        top_left_rect_right = (p2[0] - corner_radius, p2[1] + corner_radius)
        bottom_right_rect_right = (p3[0], p3[1] - corner_radius)

        all_rects = [
            [top_left_main_rect, bottom_right_main_rect],
            [top_left_rect_left, bottom_right_rect_left],
            [top_left_rect_right, bottom_right_rect_right]]

        [cv2.rectangle(src, rect[0], rect[1], color, thickness) for rect in all_rects]

    # draw straight lines
    cv2.line(src, (p1[0] + corner_radius, p1[1]), (p2[0] - corner_radius, p2[1]), color, abs(thickness), line_type)
    cv2.line(src, (p2[0], p2[1] + corner_radius), (p3[0], p3[1] - corner_radius), color, abs(thickness), line_type)
    cv2.line(src, (p3[0] - corner_radius, p4[1]), (p4[0] + corner_radius, p3[1]), color, abs(thickness), line_type)
    cv2.line(src, (p4[0], p4[1] - corner_radius), (p1[0], p1[1] + corner_radius), color, abs(thickness), line_type)

    # draw arcs
    cv2.ellipse(src, (p1[0] + corner_radius, p1[1] + corner_radius), (corner_radius, corner_radius), 180.0, 0, 90,
                color, thickness, line_type)
    cv2.ellipse(src, (p2[0] - corner_radius, p2[1] + corner_radius), (corner_radius, corner_radius), 270.0, 0, 90,
                color, thickness, line_type)
    cv2.ellipse(src, (p3[0] - corner_radius, p3[1] - corner_radius), (corner_radius, corner_radius), 0.0, 0, 90, color,
                thickness, line_type)
    cv2.ellipse(src, (p4[0] + corner_radius, p4[1] - corner_radius), (corner_radius, corner_radius), 90.0, 0, 90, color,
                thickness, line_type)
    return src

class TestRoundedRectangle(unittest.TestCase):
    def setUp(self):
        self.image = np.zeros((200, 200), dtype=np.uint8)

    def test_corner_points_calculation(self):
        top_left = (50, 50)
        bottom_right = (100, 150)
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right)
        # show_image(result_image)
        corner_radius = int(1 * (50 / 2))
        expected_image = self.image.copy()
        cv2.line(expected_image, (50 + corner_radius, 50), (100 - corner_radius, 50), 255, 1, cv2.LINE_AA)
        cv2.line(expected_image, (100, 50 + corner_radius), (100, 150 - corner_radius), 255, 1, cv2.LINE_AA)
        cv2.line(expected_image, (100 - corner_radius, 150), (50 + corner_radius, 150), 255, 1, cv2.LINE_AA)
        cv2.line(expected_image, (50, 150 - corner_radius), (50, 50 + corner_radius), 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (50 + corner_radius, 50 + corner_radius), (corner_radius, corner_radius), 180.0, 0,
                    90, 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (100 - corner_radius, 50 + corner_radius), (corner_radius, corner_radius), 270.0, 0,
                    90, 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (100 - corner_radius, 150 - corner_radius), (corner_radius, corner_radius), 0.0, 0,
                    90, 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (50 + corner_radius, 150 - corner_radius), (corner_radius, corner_radius), 90.0, 0,
                    90, 255, 1, cv2.LINE_AA)
        # show_image(expected_image)
        np.testing.assert_array_equal(result_image, expected_image)

    def test_corner_radius_calculation(self):
        top_left = (50, 50)
        bottom_right = (150, 100)
        radius = 0.5
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right, radius)
        # show_image(result_image)
        corner_radius = int(radius * (min(50, 100) / 2))
        expected_image = self.image.copy()
        cv2.line(expected_image, (50 + corner_radius, 50), (150 - corner_radius, 50), 255, 1, cv2.LINE_AA)
        cv2.line(expected_image, (150, 50 + corner_radius), (150, 100 - corner_radius), 255, 1, cv2.LINE_AA)
        cv2.line(expected_image, (150 - corner_radius, 100), (50 + corner_radius, 100), 255, 1, cv2.LINE_AA)
        cv2.line(expected_image, (50, 100 - corner_radius), (50, 50 + corner_radius), 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (50 + corner_radius, 50 + corner_radius), (corner_radius, corner_radius), 180.0, 0, 90, 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (150 - corner_radius, 50 + corner_radius), (corner_radius, corner_radius), 270.0, 0, 90, 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (150 - corner_radius, 100 - corner_radius), (corner_radius, corner_radius), 0.0, 0, 90, 255, 1, cv2.LINE_AA)
        cv2.ellipse(expected_image, (50 + corner_radius, 100 - corner_radius), (corner_radius, corner_radius), 90.0, 0, 90, 255, 1, cv2.LINE_AA)
        # show_image(expected_image)
        np.testing.assert_array_equal(result_image, expected_image)

    def test_negative_thickness(self):
        top_left = (50, 50)
        bottom_right = (100, 100)
        thickness = -1
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right, thickness=thickness)
        # show_image(result_image)
        corner_radius = int(1 * (min(50, 50) / 2))
        expected_image = correct_draw(self.image.copy(), (50, 50), (100, 50), (100, 100), (50, 100),
                                      corner_radius, thickness=thickness)
        # show_image(expected_image)
        np.testing.assert_array_equal(result_image, expected_image)

    def test_large_radius(self):
        top_left = (50, 50)
        bottom_right = (100, 100)
        radius = 2
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right, radius=radius)
        corner_radius = int(1 * (min(50, 50) / 2))  # since radius > 1, it is set to 1
        expected_image = correct_draw(self.image.copy(), (50, 50), (100, 50), (100, 100), (50, 100),
                                      corner_radius)
        np.testing.assert_array_equal(result_image, expected_image)

    def test_different_colors(self):
        top_left = (50, 50)
        bottom_right = (100, 100)
        color = 127
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right, color=color)
        # show_image(result_image)
        corner_radius = int(1 * (min(50, 50) / 2))  # since radius > 1, it is set to 1
        expected_image = correct_draw(self.image.copy(), (50, 50), (100, 50), (100, 100), (50, 100),
                                      corner_radius, color=color )
        # show_image(result_image)
        np.testing.assert_array_equal(result_image, expected_image)

    def test_different_thickness(self):
        top_left = (50, 50)
        bottom_right = (100, 100)
        thickness = 3
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right, thickness=thickness)
        # show_image(result_image)
        corner_radius = int(1 * (min(50, 50) / 2))  # since radius > 1, it is set to 1
        expected_image = correct_draw(self.image.copy(), (50, 50), (100, 50), (100, 100), (50, 100),
                                      corner_radius, thickness=thickness)
        # show_image(result_image)
        np.testing.assert_array_equal(result_image, expected_image)

    def test_line_type(self):
        top_left = (50, 50)
        bottom_right = (100, 100)
        line_type = cv2.LINE_8
        result_image = rounded_rectangle(self.image.copy(), top_left, bottom_right, line_type=line_type)
        # show_image(result_image)
        corner_radius = int(1 * (min(50, 50) / 2))  # since radius > 1, it is set to 1
        expected_image = correct_draw(self.image.copy(), (50, 50), (100, 50), (100, 100), (50, 100),
                                      corner_radius, line_type=line_type)
        # show_image(result_image)
        np.testing.assert_array_equal(result_image, expected_image)
        
if __name__ == '__main__':
    unittest.main()
