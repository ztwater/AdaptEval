WINDOW_NAME = "win"
image = cv.imread("foto.jpg", 0)
cv.namedWindow(WINDOW_NAME, cv.CV_WINDOW_AUTOSIZE)

cv.startWindowThread()

cv.imshow(WINDOW_NAME, image)
cv.waitKey()
cv.destroyAllWindows()
