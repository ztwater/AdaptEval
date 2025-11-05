Double Distance(Point a, Point b)
{
    double xdiff = a.X - b.X, ydiff = a.Y - b.Y;
    return Math.Sqrt((long)xdiff * xdiff + (long)ydiff * ydiff);
}

Boolean IsBetween(double x, double a, double b)
{
    return ((a <= b && x >= a && x <= b) || (a > b && x <= a && x >= b));
}

Double GetDistance(Point pt, Point pt1, Point pt2, out Point intersection)
{
    Double a, x, y, R;

    if (pt1.X != pt2.X) {
        a = (double)(pt2.Y - pt1.Y) / (pt2.X - pt1.X);
        x = (a * (pt.Y - pt1.Y) + a * a * pt1.X + pt.X) / (a * a + 1);
        y = a * x + pt1.Y - a * pt1.X; }
    else { x = pt1.X;  y = pt.Y; }

    if (IsBetween(x, pt1.X, pt2.X) && IsBetween(y, pt1.Y, pt2.Y)) {
        intersection = new Point((int)x, (int)y);
        R = Distance(intersection, pt); }
    else {
        double d1 = Distance(pt, pt1), d2 = Distance(pt, pt2);
        if (d1 < d2) { intersection = pt1; R = d1; }
        else { intersection = pt2; R = d2; }}

    return R;
}
