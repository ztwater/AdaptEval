CGFloat sqr(CGFloat x) { return x*x; }
CGFloat dist2(CGPoint v, CGPoint w) { return sqr(v.x - w.x) + sqr(v.y - w.y); }
CGFloat distanceToSegmentSquared(CGPoint p, CGPoint v, CGPoint w)
{
    CGFloat l2 = dist2(v, w);
    if (l2 == 0.0f) return dist2(p, v);

    CGFloat t = ((p.x - v.x) * (w.x - v.x) + (p.y - v.y) * (w.y - v.y)) / l2;
    if (t < 0.0f) return dist2(p, v);
    if (t > 1.0f) return dist2(p, w);
    return dist2(p, CGPointMake(v.x + t * (w.x - v.x), v.y + t * (w.y - v.y)));
}
CGFloat distanceToSegment(CGPoint point, CGPoint segmentPointV, CGPoint segmentPointW)
{
    return sqrtf(distanceToSegmentSquared(point, segmentPointV, segmentPointW));
}
