CREATE FUNCTION dist_to_segment(px numeric, py numeric, vx numeric, vy numeric, wx numeric, wy numeric)
  RETURNS numeric
AS $$
   declare l2 numeric;
   declare t numeric;
   declare nx numeric;
   declare ny numeric;
BEGIN 
   l2 := (vx - wx)*(vx - wx) + (vy - wy)*(vy - wy);
   IF l2 = 0 THEN
     RETURN sqrt((vx - px)*(vx - px) + (vy - py)*(vy - py));
   ELSE
     t := ((px - vx) * (wx - vx) + (py - vy) * (wy - vy)) / l2;
     t := GREATEST(0, LEAST(1, t));
     nx := vx + t * (wx - vx);
     ny := vy + t * (wy - vy);
     RETURN sqrt((nx - px)*(nx - px) + (ny - py)*(ny - py));
   END IF;
END;
$$ LANGUAGE plpgsql;
