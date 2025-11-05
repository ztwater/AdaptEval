distanceSquared = (v, w)=> Math.pow(v.x - w.x, 2) + Math.pow(v.y - w.y, 2);
distance = (v, w)=> Math.sqrt(distanceSquared(v, w));

distanceToLineSegmentSquared = (p, v, w)=> {
    l2 = distanceSquared(v, w);
    if (l2 === 0) {
        return distanceSquared(p, v);
    }
    t = ((p.x - v.x) * (w.x - v.x) + (p.y - v.y) * (w.y - v.y)) / l2;
    t = Math.max(0, Math.min(1, t));
    return distanceSquared(p, {
        x: v.x + t * (w.x - v.x),
        y: v.y + t * (w.y - v.y)
    });
}
distanceToLineSegment = (p, v, w)=> {
    return Math.sqrt(distanceToLineSegmentSquared(p, v));
}
