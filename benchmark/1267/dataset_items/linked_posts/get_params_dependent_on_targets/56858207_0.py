import numpy as np
import cv2

cam = cv2.VideoCapture(2)

while(True):
    # Capture frame-by-frame
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # You can change frame width by chaning number.

    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # You can change frame height by chaning number.

    ret, frame = cam.read()

    new_frame=cv2.rotate(frame,rotateCode = 1) 
