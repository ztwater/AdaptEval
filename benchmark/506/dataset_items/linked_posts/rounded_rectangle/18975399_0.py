/**
 * Draws a rectangle with rounded corners, the parameters are the same as in the OpenCV function @see rectangle();
 * @param cornerRadius A positive int value defining the radius of the round corners.
 * @author K
 */
void rounded_rectangle( Mat& src, Point topLeft, Point bottomRight, const Scalar lineColor, const int thickness, const int lineType , const int cornerRadius)
{
    /* corners:
     * p1 - p2
     * |     |
     * p4 - p3
     */
    Point p1 = topLeft;
    Point p2 = Point (bottomRight.x, topLeft.y);
    Point p3 = bottomRight;
    Point p4 = Point (topLeft.x, bottomRight.y);
    
    // draw straight lines
    line(src, Point (p1.x + cornerRadius, p1.y), Point (p2.x - cornerRadius, p2.y), lineColor, thickness, lineType);
    line(src, Point (p2.x, p2.y + cornerRadius), Point (p3.x, p3.y - cornerRadius), lineColor, thickness, lineType);
    line(src, Point (p4.x + cornerRadius, p4.y), Point (p3.x-cornerRadius, p3.y), lineColor, thickness, lineType);
    line(src, Point (p1.x, p1.y + cornerRadius), Point (p4.x, p4.y - cornerRadius), lineColor, thickness, lineType);
    
    // draw arcs
    ellipse( src, p1 + Point(cornerRadius, cornerRadius), Size( cornerRadius, cornerRadius ), 180.0, 0, 90, lineColor, thickness, lineType );
    ellipse( src, p2 + Point(-cornerRadius, cornerRadius), Size( cornerRadius, cornerRadius ), 270.0, 0, 90, lineColor, thickness, lineType );
    ellipse( src, p3 + Point(-cornerRadius, -cornerRadius), Size( cornerRadius, cornerRadius ), 0.0, 0, 90, lineColor, thickness, lineType );
    ellipse( src, p4 + Point(cornerRadius, -cornerRadius), Size( cornerRadius, cornerRadius ), 90.0, 0, 90, lineColor, thickness, lineType );
}
