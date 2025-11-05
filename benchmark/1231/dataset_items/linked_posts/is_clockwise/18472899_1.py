double sum = 0.0;
Vector v1 = vertices[vertices.Count - 1]; // or vertices[^1] with
                                          // C# 8.0+ and .NET Core
for (int i = 0; i < vertices.Count; i++) {
    Vector v2 = vertices[i];
    sum += (v2.X - v1.X) * (v2.Y + v1.Y);
    v1 = v2;
}
return sum > 0.0;
