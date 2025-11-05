    # Define the Hough transform parameters
    rho,theta,threshold,min,max = 1, np.pi/180, 30, 40, 60  

    image = ima.astype(np.uint8) # assuming that ima is an image.

    # Run Hough on edge detected image
    lines = cv2.HoughLinesP(sob, rho, theta, threshold, np.array([]), min, max)

    # Iterate over the output "lines" and draw lines on the blank 
    line_image = np.array([[0 for col in range(x)] for row in range(y)]).astype(np.uint8)

    for line in lines: # lines are series of (x,y) coordinates
        for x1,y1,x2,y2 in line:
            cv2.line(line_image, (x1,y1), (x2,y2), (255,0,0), 10)
