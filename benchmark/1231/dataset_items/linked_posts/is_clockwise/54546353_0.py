// https://en.wikipedia.org/wiki/Curve_orientation#Orientation_of_a_simple_polygon
public static WindingOrder DetermineWindingOrder(IList<Vector2> vertices)
{
    int nVerts = vertices.Count;
    // If vertices duplicates first as last to represent closed polygon,
    // skip last.
    Vector2 lastV = vertices[nVerts - 1];
    if (lastV.Equals(vertices[0]))
        nVerts -= 1;
    int iMinVertex = FindCornerVertex(vertices);
    // Orientation matrix:
    //     [ 1  xa  ya ]
    // O = | 1  xb  yb |
    //     [ 1  xc  yc ]
    Vector2 a = vertices[WrapAt(iMinVertex - 1, nVerts)];
    Vector2 b = vertices[iMinVertex];
    Vector2 c = vertices[WrapAt(iMinVertex + 1, nVerts)];
    // determinant(O) = (xb*yc + xa*yb + ya*xc) - (ya*xb + yb*xc + xa*yc)
    double detOrient = (b.X * c.Y + a.X * b.Y + a.Y * c.X) - (a.Y * b.X + b.Y * c.X + a.X * c.Y);

    // TBD: check for "==0", in which case is not defined?
    // Can that happen?  Do we need to check other vertices / eliminate duplicate vertices?
    WindingOrder result = detOrient > 0
            ? WindingOrder.Clockwise
            : WindingOrder.CounterClockwise;
    return result;
}

public enum WindingOrder
{
    Clockwise,
    CounterClockwise
}

// Find vertex along one edge of bounding box.
// In this case, we find smallest y; in case of tie also smallest x.
private static int FindCornerVertex(IList<Vector2> vertices)
{
    int iMinVertex = -1;
    float minY = float.MaxValue;
    float minXAtMinY = float.MaxValue;
    for (int i = 0; i < vertices.Count; i++)
    {
        Vector2 vert = vertices[i];
        float y = vert.Y;
        if (y > minY)
            continue;
        if (y == minY)
            if (vert.X >= minXAtMinY)
                continue;

        // Minimum so far.
        iMinVertex = i;
        minY = y;
        minXAtMinY = vert.X;
    }

    return iMinVertex;
}

// Return value in (0..n-1).
// Works for i in (-n..+infinity).
// If need to allow more negative values, need more complex formula.
private static int WrapAt(int i, int n)
{
    // "+n": Moves (-n..) up to (0..).
    return (i + n) % n;
}
