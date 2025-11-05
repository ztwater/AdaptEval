public bool IsClockwise(IList<Vector> vertices)
{
    double sum = 0.0;
    for (int i = 0; i < vertices.Count; i++) {
        Vector v1 = vertices[i];
        Vector v2 = vertices[(i + 1) % vertices.Count];
        sum += (v2.X - v1.X) * (v2.Y + v1.Y);
    }
    return sum > 0.0;
}
