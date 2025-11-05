def DrawRoundedRectangle(img, topLeft, bottomRight, radius=1, color=255, thickness=1, line_type=cv.LINE_AA):

min_half = int(min((bottomRight[0] - topLeft[0]), (bottomRight[1] - topLeft[1])) * 0.5)
radius = min(radius, min_half)

# /* corners:
#  * p1 - p2
#  * |     |
#  * p4 - p3
#  */
p1 = topLeft
p2 = (bottomRight[0], topLeft[1])
p3 = bottomRight
p4 = (topLeft[0], bottomRight[1])

if(thickness < 0):
    # // draw rectangle
    cv.rectangle(img, (p1[0] + radius, p1[1]),  (p3[0] - radius, p3[1]), color, thickness, line_type)
    cv.rectangle(img, (p1[0], p1[1] + radius),  (p3[0], p3[1] - radius), color, thickness, line_type)
else:
    # // draw straight lines
    cv.line(img, (p1[0] + radius, p1[1]),  (p2[0] - radius, p2[1]), color, thickness, line_type);
    cv.line(img, (p2[0], p2[1] + radius),  (p3[0], p3[1] - radius), color, thickness, line_type);
    cv.line(img, (p4[0] + radius, p4[1]),  (p3[0]-radius, p3[1]), color, thickness, line_type);
    cv.line(img, (p1[0], p1[1] + radius),  (p4[0], p4[1] - radius), color, thickness, line_type);

# // draw arcs
if(radius > 0):
    cv.ellipse( img, (p1[0] + radius, p1[1] + radius), ( radius, radius ), 180.0, 0, 90, color, thickness, line_type );
    cv.ellipse( img, (p2[0] - radius, p2[1] + radius), ( radius, radius ), 270.0, 0, 90, color, thickness, line_type );
    cv.ellipse( img, (p3[0] - radius, p3[1] - radius), ( radius, radius ), 0.0, 0, 90, color, thickness, line_type );
    cv.ellipse( img, (p4[0] + radius, p4[1] - radius), ( radius, radius ), 90.0, 0, 90, color, thickness, line_type );
