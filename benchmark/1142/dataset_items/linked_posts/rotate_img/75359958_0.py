import cv2
import numpy as np

img = np.zeros((200, 200, 3), dtype=np.uint8)

# Breaks
img = np.require(img, requirements=["F_CONTIGUOUS"])

# img = np.require(img, requirements=["C_CONTIGUOUS"])  # Fixes it
# img = img.copy()  # Also fixes it

cv2.line(img, (10, 10), (100, 100), (255,0,0), 5)
