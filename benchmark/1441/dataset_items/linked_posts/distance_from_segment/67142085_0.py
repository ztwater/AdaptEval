func minimum_distance(v: Vector2, w: Vector2, p: Vector2):
    # Return minimum distance between line segment vw and point p
    var l2: float = (v - w).length_squared()  # i.e. |w-v|^2 -  avoid a sqrt
    if l2 == 0.0:
        return p.distance_to(v) # v == w case

    # Consider the line extending the segment, parameterized as v + t (w - v).
    # We find projection of point p onto the line.
    # It falls where t = [(p-v) . (w-v)] / |w-v|^2
    # We clamp t from [0,1] to handle points outside the segment vw.
    var t: float = max(0, min(1, (p - v).dot(w - v) / l2))
    var projection: Vector2 = v + t * (w - v)  # Projection falls on the segment
    
    return p.distance_to(projection)
