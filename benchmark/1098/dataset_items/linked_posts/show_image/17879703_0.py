 import cv2

 threadDie = True # change this to false elsewhere to stop getting the video
 def getVideo(Message):
          print Message
          print "Opening url"
          video = cv2.VideoCapture("rtsp://username:passwordp@IpAddress:554/axis-media/media.amp")

          print "Opened url"
          fourcc = cv2.cv.CV_FOURCC('X','V','I','D')
          fps = 25.0 # or 30.0 for a better quality stream
          writer = cv2.VideoWriter('out.avi', fourcc,fps, (640,480),1)
          i = 0

          print "Reading frames "
          while threadDie:
                  ret, img = video.read()
                  print "frame number: ",i
                  i=i+1
                  writer.write(img)
          del(video)


          print "Finished capturing video"
