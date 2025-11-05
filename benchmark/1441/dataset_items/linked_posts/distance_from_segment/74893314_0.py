public static FP DistanceToLineSegment(FPVector3 a, FPVector3 b, FPVector3 point)
{
  var d = b - a;
  var s = d.SqrMagnitude;
  var ds = d / s;
  var lambda = FPVector3.Dot(point - a, ds);
  var p = FPMath.Clamp01(lambda) * d;
  return (a + p - point).Magnitude;
}
