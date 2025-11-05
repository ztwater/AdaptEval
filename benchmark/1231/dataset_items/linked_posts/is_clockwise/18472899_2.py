public static bool IsClockwise(IList<(double X, double Y)> vertices)
{
    double sum = 0.0;
    var v1 = vertices[^1];
    for (int i = 0; i < vertices.Count; i++) {
        var v2 = vertices[i];
        sum += (v2.X - v1.X) * (v2.Y + v1.Y);
        Console.WriteLine($"(({v2.X,2}) - ({v1.X,2})) * (({v2.Y,2}) + ({v1.Y,2})) = {(v2.X - v1.X) * (v2.Y + v1.Y)}");
        v1 = v2;
    }
    Console.WriteLine(sum);
    return sum > 0.0;
}

public static void Test()
{
    Console.WriteLine(IsClockwise(new[] { (-5.0, -5.0), (-5.0, 5.0), (5.0, 5.0), (5.0, -5.0) }));

    // infinity Symbol
    //Console.WriteLine(IsClockwise(new[] { (-5.0, -5.0), (-5.0, 5.0), (5.0, -5.0), (5.0, 5.0) }));
}
