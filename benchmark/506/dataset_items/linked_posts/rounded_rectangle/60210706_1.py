top_left = (0, 0)
bottom_right = (500, 800)
color = (255, 255, 255)
image_size = (500, 800, 3)
img = np.zeros(image_size)
img = rounded_rectangle(img, top_left, bottom_right, color=color, radius=0.5, thickness=-1)

cv2.imshow('rounded_rect', img)
cv2.waitKey(0)
