def draw_line(var_0, var_1, var_2, var_3, var_4):
    x1, y1, x2, y2 = *var_1, *var_2
    var_5 = np.pi - np.arctan2(y1 - y2, x1 - x2)
    var_6 = int(np.sin(var_5) * var_4 / 2)
    var_7 = int(np.cos(var_5) * var_4 / 2)
    var_8 = [
        [x1 + var_6, y1 + var_7],
        [x1 - var_6, y1 - var_7],
        [x2 - var_6, y2 - var_7],
        [x2 + var_6, y2 + var_7]
    ]
    cv2.fillPoly(var_0, [np.array(var_8)], var_3)
