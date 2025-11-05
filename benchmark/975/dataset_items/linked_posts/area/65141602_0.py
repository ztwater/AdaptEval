points = np.array([[0,0],[10,0],[10,10],[0,10]])
area = cv2.contourArea(points)
print(area) # 100.0
