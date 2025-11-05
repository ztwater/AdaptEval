public static double MinimumDistanceToLineSegment(this Point p,
    Line line)
{
    var v = line.StartPoint;
    var w = line.EndPoint;

    double lengthSquared = DistanceSquared(v, w);

    if (lengthSquared == 0.0)
        return Distance(p, v);

    double t = Math.Max(0, Math.Min(1, DotProduct(p - v, w - v) / lengthSquared));
    var projection = v + t * (w - v);

    return Distance(p, projection);
}

public static double Distance(Point a, Point b)
{
    return Math.Sqrt(DistanceSquared(a, b));
}

public static double DistanceSquared(Point a, Point b)
{
    var d = a - b;
    return DotProduct(d, d);
}

public static double DotProduct(Point a, Point b)
{
    return (a.X * b.X) + (a.Y * b.Y);
}
