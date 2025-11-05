while(cap.isOpened()):
 ret, frame = cap.read()  
 if ret == False:
        cap.release()
        cv2.waitKey(1)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
