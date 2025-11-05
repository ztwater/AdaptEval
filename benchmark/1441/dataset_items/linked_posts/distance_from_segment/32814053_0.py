public class LineSegment
{
    private readonly Vector _offset;
    private readonly Vector _vector;

    public LineSegment(Point start, Point end)
    {
        _offset = (Vector)start;
        _vector = (Vector)(end - _offset);
    }

    public double DistanceTo(Point pt)
    {
        var v = (Vector)pt - _offset;

        // first, find a projection point on the segment in parametric form (0..1)
        var p = (v * _vector) / _vector.LengthSquared;

        // and limit it so it lays inside the segment
        p = Math.Min(Math.Max(p, 0), 1);

        // now, find the distance from that point to our point
        return (_vector * p - v).Length;
    }
}
