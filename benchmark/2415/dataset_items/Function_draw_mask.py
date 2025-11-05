import cv2
import numpy as np

def draw_line(img, pt1, pt2, color, thickness):
    #Function found at : https://stackoverflow.com/questions/73050416/how-to-draw-a-line-line-with-rectangular-corners-with-opencv-and-python
    #From: https://stackoverflow.com/users/13552470/ann-zen
    x1, y1, x2, y2 = *pt1, *pt2
    theta = np.pi - np.arctan2(y1 - y2, x1 - x2)
    dx = int(np.sin(theta) * thickness / 2)
    dy = int(np.cos(theta) * thickness / 2)
    pts = [
        [x1 + dx, y1 + dy],
        [x1 - dx, y1 - dy],
        [x2 - dx, y2 - dy],
        [x2 + dx, y2 + dy]
    ]
    cv2.fillPoly(img, [np.array(pts)], color)
    return img