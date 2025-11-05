import cv2
import numpy as np

def draw_line(img, pt1, pt2, color, thickness):
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

img = np.full((600, 600, 3), 255, np.uint8)

pt1 = np.random.randint(0, 600, 2)
pt2 = np.random.randint(0, 600, 2)

draw_line(img, pt1, pt2, (0, 0, 0), 15)
cv2.line(img, pt1, pt2, (255, 255, 255), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
