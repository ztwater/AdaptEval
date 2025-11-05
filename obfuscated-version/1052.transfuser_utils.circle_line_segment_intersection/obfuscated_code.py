def circle_line_segment_intersection(var_0, var_1, var_2, var_3, var_4=True, var_5=1e-9):
    """ Find the points at which a circle intersects a line-segment.  This can happen at 0, 1, or 2 points.

    :param circle_center: The (x, y) location of the circle center
    :param circle_radius: The radius of the circle
    :param pt1: The (x, y) location of the first point of the segment
    :param pt2: The (x, y) location of the second point of the segment
    :param full_line: True to find intersections along full line - not just in the segment.  False will just return intersections within the segment.
    :param tangent_tol: Numerical tolerance at which we decide the intersections are close enough to consider it a tangent
    :return Sequence[Tuple[float, float]]: A list of length 0, 1, or 2, where each element is a point at which the circle intercepts a line segment.

    Note: We follow: http://mathworld.wolfram.com/Circle-LineIntersection.html
    """

    (p1x, p1y), (p2x, p2y), (cx, cy) = var_2, var_3, var_0
    (x1, y1), (x2, y2) = (p1x - cx, p1y - cy), (p2x - cx, p2y - cy)
    dx, dy = (x2 - x1), (y2 - y1)
    var_6 = (dx ** 2 + dy ** 2)**.5
    var_7 = x1 * y2 - x2 * y1
    var_8 = var_1 ** 2 * var_6 ** 2 - var_7 ** 2

    if var_8 < 0:  # No intersection between circle and line
        return []
    else:  # There may be 0, 1, or 2 intersections with the segment
        var_9 = [
            (cx + (var_7 * dy + sign * (-1 if dy < 0 else 1) * dx * var_8**.5) / var_6 ** 2,
             cy + (-var_7 * dx + sign * abs(dy) * var_8**.5) / var_6 ** 2)
            for sign in ((1, -1) if dy < 0 else (-1, 1))]  # This makes sure the order along the segment is correct
        if not var_4:  # If only considering the segment, filter out intersections that do not fall within the segment
            var_10 = [(xi - p1x) / dx if abs(dx) > abs(dy) else (yi - p1y) / dy for xi, yi in var_9]
            var_9 = [pt for pt, frac in zip(var_9, var_10) if 0 <= frac <= 1]
        if len(var_9) == 2 and abs(var_8) <= var_5:  # If line is tangent to circle, return just one point (as both intersections have same location)
            return [var_9[0]]
        else:
            return var_9
