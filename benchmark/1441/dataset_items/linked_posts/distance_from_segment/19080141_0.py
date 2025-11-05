let pointToLineSegmentDistance (a: Vector, b: Vector) (c: Vector) =
  let d = b - a
  let s = d.Length
  let lambda = (c - a) * d / s
  let p = (lambda |> max 0.0 |> min s) * d / s
  (a + p - c).Length
