import 'dart:math' as math;
 class Utils {
   static double shortestDistance(Point p1, Point p2, Point p3){
      double px = p2.x - p1.x;
      double py = p2.y - p1.y;
      double temp = (px*px) + (py*py);
      double u = ((p3.x - p1.x)*px + (p3.y - p1.y)* py) /temp;
      if(u>1){
        u=1;
      }
      else if(u<0){
        u=0;
      }
      double x = p1.x + u*px;
      double y = p1.y + u*py;
      double dx = x - p3.x;
      double dy = y - p3.y;
      double dist = math.sqrt(dx*dx+dy*dy);
      return dist;
   }
}

class Point {
  double x;
  double y;
  Point(this.x, this.y);
}
