import numpy as np
from PIL import ImageGrab
import cv2

angle = -90
scale = 1.0

while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    new = cv2.rotate(frame,rotateCode = 0)# this is the line to rotate the image
    true = cv2.resize(new, (0,0), fx = 0.6, fy = 0.6) # with fxand fy u can control the size
    cv2.imshow('output', true)
    if cv2.waitKey(1) == 27:
        break


cv2.destroyAllWindows()
