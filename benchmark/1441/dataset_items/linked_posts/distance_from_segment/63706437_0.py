CREATE FUNCTION dist_to_segment(px double, py double, vx double, vy double, wx double, wy double)
  RETURNS double
BEGIN atomic
   declare l2 double;
   declare t double;
   declare nx double;
   declare ny double;
   set l2 =(vx - wx)*(vx - wx) + (vy - wy)*(vy - wy);
   IF l2 = 0 THEN
     RETURN sqrt((vx - px)*(vx - px) + (vy - py)*(vy - py));
   ELSE
     set t = ((px - vx) * (wx - vx) + (py - vy) * (wy - vy)) / l2;
     set t = GREATEST(0, LEAST(1, t));
     set nx=vx + t * (wx - vx);
     set ny=vy + t * (wy - vy);
     RETURN sqrt((nx - px)*(nx - px) + (ny - py)*(ny - py));
   END IF;
END;
