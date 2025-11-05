Function DistanceToSegment(x As Double, y As Double, x1 As Double, y1 As Double, x2 As Double, y2 As Double)

  Dim A As Double
  A = x - x1
  Dim B As Double
  B = y - y1
  Dim C  As Double
  C = x2 - x1
  Dim D As Double
  D = y2 - y1

  Dim dot As Double
  dot = A * C + B * D
  Dim len_sq As Double
  len_sq = C * C + D * D
  Dim param As Double
  param = -1

  If (len_sq <> 0) Then
      param = dot / len_sq
  End If

  Dim xx As Double
  Dim yy As Double

  If (param < 0) Then
    xx = x1
    yy = y1
  ElseIf (param > 1) Then
    xx = x2
    yy = y2
  Else
    xx = x1 + param * C
    yy = y1 + param * D
  End If

  Dim dx As Double
  dx = x - xx
  Dim dy As Double
  dy = y - yy

  DistanceToSegment = Math.Sqr(dx * dx + dy * dy)

End Function
