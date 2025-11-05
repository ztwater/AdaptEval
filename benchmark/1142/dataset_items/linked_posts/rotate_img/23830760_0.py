found = np.array(found)
boxes = cv2.groupRectangles(found.tolist(), 1, 2)
