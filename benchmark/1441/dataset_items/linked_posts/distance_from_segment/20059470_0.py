public double Distance(Point a, Point b, Point c)
{
    // normalize points
    Point cn = new Point(c.X - a.X, c.Y - a.Y);
    Point bn = new Point(b.X - a.X, b.Y - a.Y);

    double angle = Math.Atan2(bn.Y, bn.X) - Math.Atan2(cn.Y, cn.X);
    double abLength = Math.Sqrt(bn.X*bn.X + bn.Y*bn.Y);

    return Math.Sin(angle)*abLength;
}
