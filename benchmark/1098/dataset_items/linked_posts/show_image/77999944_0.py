import cv2

cam_port = 0 # Your camera seed

cam = cv2.VideoCapture(cam_port)
while cam.isOpened():
   result, image = cam.read()
   if result:
     cv2.imshow("Real-time Capture", image)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break # Exit the real-time capture 

cam.release()
cv2.destroyAllWindows()
cv2.waitKey(1). # Need this line to wait for the destroy actions to complete
