function DistancePtToSegment( pt, pt1, pt2: TPoint): double;
var
   a, b, c, d: double;
   len_sq: double;
   param: double;
   xx, yy: double;
   dx, dy: double;
begin
   a := pt.x - pt1.x;
   b := pt.y - pt1.y;
   c := pt2.x - pt1.x;
   d := pt2.y - pt1.y;

   len_sq := (c * c) + (d * d);
   param := -1;

   if (len_sq <> 0) then
   begin
      param := ((a * c) + (b * d)) / len_sq;
   end;

   if param < 0 then
   begin
      xx := pt1.x;
      yy := pt1.y;
   end
   else if param > 1 then
   begin
      xx := pt2.x;
      yy := pt2.y;
   end
   else begin
      xx := pt1.x + param * c;
      yy := pt1.y + param * d;
   end;

   dx := pt.x - xx;
   dy := pt.y - yy;
   result := sqrt( (dx * dx) + (dy * dy))
end;
