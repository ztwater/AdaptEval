def addRoundedRectangleBorder(img):
    height, width, channels = img.shape

    border_radius = int(width * random.randint(1, 10)/100.0)
    line_thickness = int(max(width, height) * random.randint(1, 3)/100.0)
    edge_shift = int(line_thickness/2.0)

    red = random.randint(230,255)
    green = random.randint(230,255)
    blue = random.randint(230,255)
    color = (blue, green, red)

    #draw lines
    #top
    cv2.line(img, (border_radius, edge_shift), 
    (width - border_radius, edge_shift), (blue, green, red), line_thickness)
    #bottom
    cv2.line(img, (border_radius, height-line_thickness), 
    (width - border_radius, height-line_thickness), (blue, green, red), line_thickness)
    #left
    cv2.line(img, (edge_shift, border_radius), 
    (edge_shift, height  - border_radius), (blue, green, red), line_thickness)
    #right
    cv2.line(img, (width - line_thickness, border_radius), 
    (width - line_thickness, height  - border_radius), (blue, green, red), line_thickness)

    #corners
    cv2.ellipse(img, (border_radius+ edge_shift, border_radius+edge_shift), 
    (border_radius, border_radius), 180, 0, 90, color, line_thickness)
    cv2.ellipse(img, (width-(border_radius+line_thickness), border_radius), 
    (border_radius, border_radius), 270, 0, 90, color, line_thickness)
    cv2.ellipse(img, (width-(border_radius+line_thickness), height-(border_radius + line_thickness)), 
    (border_radius, border_radius), 10, 0, 90, color, line_thickness)
    cv2.ellipse(img, (border_radius+edge_shift, height-(border_radius + line_thickness)), 
    (border_radius, border_radius), 90, 0, 90, color, line_thickness)

    return img
