function DrawRoundedRectangle(img, topLeft, bottomRight, radius=1, color=255, thickness=1, line_type=cv.LINE_AA){

let min_half = Math.floor(Math.min((bottomRight.x - topLeft.x), (bottomRight.y - topLeft.y)) * 0.5)
radius = Math.min(radius, min_half)

/* corners:
#  * p1 - p2
#  * |     |
#  * p4 - p3
#  */
let p1 = topLeft
let p2 = new cv.Point(bottomRight.x, topLeft.y)
let p3 = bottomRight
let p4 = new cv.Point(topLeft.x, bottomRight.y)

if(thickness < 0){
    // draw rectangle
    cv.rectangle(img, new cv.Point(p1.x + radius, p1.y),  new cv.Point(p3.x - radius, p3.y), color, thickness, line_type)
    cv.rectangle(img, new cv.Point(p1.x, p1.y + radius),  new cv.Point(p3.x, p3.y - radius), color, thickness, line_type)
}
else{
    // draw straight lines
    cv.line(img, new cv.Point(p1.x + radius, p1.y),  new cv.Point(p2.x - radius, p2.y), color, thickness, line_type);
    cv.line(img, new cv.Point(p2.x, p2.y + radius),  new cv.Point(p3.x, p3.y - radius), color, thickness, line_type);
    cv.line(img, new cv.Point(p4.x + radius, p4.y),  new cv.Point(p3.x-radius, p3.y), color, thickness, line_type);
    cv.line(img, new cv.Point(p1.x, p1.y + radius),  new cv.Point(p4.x, p4.y - radius), color, thickness, line_type);
}
// draw arcs
if(radius > 0){
    cv.ellipse( img, new cv.Point(p1.x + radius, p1.y + radius), new cv.Size( radius, radius ), 180.0, 0, 90, color, thickness, line_type );
    cv.ellipse( img, new cv.Point(p2.x - radius, p2.y + radius), new cv.Size( radius, radius ), 270.0, 0, 90, color, thickness, line_type );
    cv.ellipse( img, new cv.Point(p3.x - radius, p3.y - radius), new cv.Size( radius, radius ), 0.0, 0, 90, color, thickness, line_type );
    cv.ellipse( img, new cv.Point(p4.x + radius, p4.y - radius), new cv.Size( radius, radius ), 90.0, 0, 90, color, thickness, line_type );
}
}
