public float DistanceOfPointToLine2(PointF p1, PointF p2, PointF p)
{
  //          (y1-y2)x + (x2-x1)y + (x1y2-x2y1)
  //d(P,L) = --------------------------------
  //         sqrt( (x2-x1)pow2 + (y2-y1)pow2 )

  double ch = (p1.Y - p2.Y) * p.X + (p2.X - p1.X) * p.Y + (p1.X * p2.Y - p2.X * p1.Y);
  double del = Math.Sqrt(Math.Pow(p2.X - p1.X, 2) + Math.Pow(p2.Y - p1.Y, 2));
  double d = ch / del;
  return (float)d;
}
