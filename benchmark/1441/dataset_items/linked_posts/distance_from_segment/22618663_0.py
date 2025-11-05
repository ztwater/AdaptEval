public static bool PointSegmentDistanceSquared(PointF point, PointF lineStart, PointF lineEnd, out double distance, out PointF intersectPoint)
{
    const double kMinSegmentLenSquared = 0.00000001; // adjust to suit.  If you use float, you'll probably want something like 0.000001f
    const double kEpsilon = 1.0E-14; // adjust to suit.  If you use floats, you'll probably want something like 1E-7f
    double dX = lineEnd.X - lineStart.X;
    double dY = lineEnd.Y - lineStart.Y;
    double dp1X = point.X - lineStart.X;
    double dp1Y = point.Y - lineStart.Y;
    double segLenSquared = (dX * dX) + (dY * dY);
    double t = 0.0;

    if (segLenSquared >= -kMinSegmentLenSquared && segLenSquared <= kMinSegmentLenSquared)
    {
        // segment is a point.
        intersectPoint = lineStart;
        t = 0.0;
        distance = ((dp1X * dp1X) + (dp1Y * dp1Y));
    }
    else
    {
        // Project a line from p to the segment [p1,p2].  By considering the line
        // extending the segment, parameterized as p1 + (t * (p2 - p1)),
        // we find projection of point p onto the line. 
        // It falls where t = [(p - p1) . (p2 - p1)] / |p2 - p1|^2
        t = ((dp1X * dX) + (dp1Y * dY)) / segLenSquared;
        if (t < kEpsilon)
        {
            // intersects at or to the "left" of first segment vertex (lineStart.X, lineStart.Y).  If t is approximately 0.0, then
            // intersection is at p1.  If t is less than that, then there is no intersection (i.e. p is not within
            // the 'bounds' of the segment)
            if (t > -kEpsilon)
            {
                // intersects at 1st segment vertex
                t = 0.0;
            }
            // set our 'intersection' point to p1.
            intersectPoint = lineStart;
            // Note: If you wanted the ACTUAL intersection point of where the projected lines would intersect if
            // we were doing PointLineDistanceSquared, then intersectPoint.X would be (lineStart.X + (t * dx)) and intersectPoint.Y would be (lineStart.Y + (t * dy)).
        }
        else if (t > (1.0 - kEpsilon))
        {
            // intersects at or to the "right" of second segment vertex (lineEnd.X, lineEnd.Y).  If t is approximately 1.0, then
            // intersection is at p2.  If t is greater than that, then there is no intersection (i.e. p is not within
            // the 'bounds' of the segment)
            if (t < (1.0 + kEpsilon))
            {
                // intersects at 2nd segment vertex
                t = 1.0;
            }
            // set our 'intersection' point to p2.
            intersectPoint = lineEnd;
            // Note: If you wanted the ACTUAL intersection point of where the projected lines would intersect if
            // we were doing PointLineDistanceSquared, then intersectPoint.X would be (lineStart.X + (t * dx)) and intersectPoint.Y would be (lineStart.Y + (t * dy)).
        }
        else
        {
            // The projection of the point to the point on the segment that is perpendicular succeeded and the point
            // is 'within' the bounds of the segment.  Set the intersection point as that projected point.
            intersectPoint = new PointF((float)(lineStart.X + (t * dX)), (float)(lineStart.Y + (t * dY)));
        }
        // return the squared distance from p to the intersection point.  Note that we return the squared distance
        // as an optimization because many times you just need to compare relative distances and the squared values
        // works fine for that.  If you want the ACTUAL distance, just take the square root of this value.
        double dpqX = point.X - intersectPoint.X;
        double dpqY = point.Y - intersectPoint.Y;

        distance = ((dpqX * dpqX) + (dpqY * dpqY));
    }

    return true;
}
