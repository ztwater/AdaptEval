import cv2 as cv
cv.namedWindow("image")
img = cv.imread("image_name.jpg")
cv.imshow("image",img)

cv.waitKey(5000) # 5 sec delay before image window closes
cv.destroyWindow("image")
