def draw_line(img, pt1, pt2, color, thickness):
    x1, y1, x2, y2 = *pt1, *pt2
    theta = np.pi - np.arctan2(y1 - y2, x1 - x2)
    dx = int(np.sin(theta) * thickness / 2)
    dy = int(np.cos(theta) * thickness / 2)
    pts = [
        [x1 + dx, y1 + dy],
        [x1 - dx, y1 - dy],
        [x2 - dx, y2 - dy],
        [x2 + dx, y2 + dy]
    ]
    cv2.fillPoly(img, [np.array(pts)], color)
