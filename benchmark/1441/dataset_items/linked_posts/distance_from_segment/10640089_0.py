function Dot(const p1, p2: PointF): double;
begin
  Result := p1.x * p2.x + p1.y * p2.y;
end;
function SubPoint(const p1, p2: PointF): PointF;
begin
  result.x := p1.x - p2.x;
  result.y := p1.y - p2.y;
end;

function ShortestDistance2(const p,v,w : PointF) : double;
var
  l2,t : double;
  projection,tt: PointF;
begin
  // Return minimum distance between line segment vw and point p
  //l2 := length_squared(v, w);  // i.e. |w-v|^2 -  avoid a sqrt
  l2 := Distance(v,w);
  l2 := MPower(l2,2);
  if (l2 = 0.0) then begin
    result:= Distance(p, v);   // v == w case
    exit;
  end;
  // Consider the line extending the segment, parameterized as v + t (w - v).
  // We find projection of point p onto the line.
  // It falls where t = [(p-v) . (w-v)] / |w-v|^2
  t := Dot(SubPoint(p,v),SubPoint(w,v)) / l2;
  if (t < 0.0) then begin
    result := Distance(p, v);       // Beyond the 'v' end of the segment
    exit;
  end
  else if (t > 1.0) then begin
    result := Distance(p, w);  // Beyond the 'w' end of the segment
    exit;
  end;
  //projection := v + t * (w - v);  // Projection falls on the segment
  tt.x := v.x + t * (w.x - v.x);
  tt.y := v.y + t * (w.y - v.y);
  result := Distance(p, tt);
end;
