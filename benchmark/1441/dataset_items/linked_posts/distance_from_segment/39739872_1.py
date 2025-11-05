distanceSquared = (v, w)-> (v.x - w.x) ** 2 + (v.y - w.y) ** 2
distance = (v, w)-> Math.sqrt(distanceSquared(v, w))

distanceToLineSegmentSquared = (p, v, w)->
    l2 = distanceSquared(v, w)
    return distanceSquared(p, v) if l2 is 0
    t = ((p.x - v.x) * (w.x - v.x) + (p.y - v.y) * (w.y - v.y)) / l2
    t = Math.max(0, Math.min(1, t))
    distanceSquared(p, {
        x: v.x + t * (w.x - v.x)
        y: v.y + t * (w.y - v.y)
    })

distanceToLineSegment = (p, v, w)->
    Math.sqrt(distanceToLineSegmentSquared(p, v, w))
