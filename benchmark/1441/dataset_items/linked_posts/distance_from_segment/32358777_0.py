static double sqr(double x) {
    return x * x;
}
static double dist2(DoublePoint v, DoublePoint w) {
    return sqr(v.x - w.x) + sqr(v.y - w.y);
}
static double distToSegmentSquared(DoublePoint p, DoublePoint v, DoublePoint w) {
    double l2 = dist2(v, w);
    if (l2 == 0) return dist2(p, v);
    double t = ((p.x - v.x) * (w.x - v.x) + (p.y - v.y) * (w.y - v.y)) / l2;
    if (t < 0) return dist2(p, v);
    if (t > 1) return dist2(p, w);
    return dist2(p, new DoublePoint(
            v.x + t * (w.x - v.x),
            v.y + t * (w.y - v.y)
    ));
}
static double distToSegment(DoublePoint p, DoublePoint v, DoublePoint w) {
    return Math.sqrt(distToSegmentSquared(p, v, w));
}
static class DoublePoint {
    public double x;
    public double y;

    public DoublePoint(double x, double y) {
        this.x = x;
        this.y = y;
    }
}
