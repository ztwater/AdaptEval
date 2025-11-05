import cv2 as cv
import time

WINDOW_NAME = "win"

image = cv.imread("ela.jpg", cv.CV_LOAD_IMAGE_COLOR)
cv.namedWindow(WINDOW_NAME, cv.CV_WINDOW_AUTOSIZE)
initialtime = time.time()

cv.startWindowThread()

while (time.time() - initialtime < 5):
  print "in first while"
cv.imshow(WINDOW_NAME, image)
cv.waitKey(1000)

cv.waitKey(1)
cv.destroyAllWindows()
cv.waitKey(1)

initialtime = time.time()
while (time.time() - initialtime < 6):
    print "in second while"
