   public struct MyVector
   {
      private readonly double _x, _y;


      // Constructor
      public MyVector(double x, double y)
      {
         _x = x;
         _y = y;
      }


      // Distance from this point to another point, squared
      private double DistanceSquared(MyVector otherPoint)
      {
         double dx = otherPoint._x - this._x;
         double dy = otherPoint._y - this._y;
         return dx * dx + dy * dy;
      }


      // Find the distance from this point to a line segment (which is not the same as from this 
      //  point to anywhere on an infinite line). Also returns the closest point.
      public double DistanceToLineSegment(MyVector lineSegmentPoint1, MyVector lineSegmentPoint2,
                                          out MyVector closestPoint)
      {
         return Math.Sqrt(DistanceToLineSegmentSquared(lineSegmentPoint1, lineSegmentPoint2, 
                          out closestPoint));
      }


      // Same as above, but avoid using Sqrt(), saves a new nanoseconds in cases where you only want 
      //  to compare several distances to find the smallest or largest, but don't need the distance
      public double DistanceToLineSegmentSquared(MyVector lineSegmentPoint1, 
                                              MyVector lineSegmentPoint2, out MyVector closestPoint)
      {
         // Compute length of line segment (squared) and handle special case of coincident points
         double segmentLengthSquared = lineSegmentPoint1.DistanceSquared(lineSegmentPoint2);
         if (segmentLengthSquared < 1E-7f)  // Arbitrary "close enough for government work" value
         {
            closestPoint = lineSegmentPoint1;
            return this.DistanceSquared(closestPoint);
         }

         // Use the magic formula to compute the "projection" of this point on the infinite line
         MyVector lineSegment = lineSegmentPoint2 - lineSegmentPoint1;
         double t = (this - lineSegmentPoint1).DotProduct(lineSegment) / segmentLengthSquared;

         // Handle the two cases where the projection is not on the line segment, and the case where 
         //  the projection is on the segment
         if (t <= 0)
            closestPoint = lineSegmentPoint1;
         else if (t >= 1)
            closestPoint = lineSegmentPoint2;
         else 
            closestPoint = lineSegmentPoint1 + (lineSegment * t);
         return this.DistanceSquared(closestPoint);
      }


      public double DotProduct(MyVector otherVector)
      {
         return this._x * otherVector._x + this._y * otherVector._y;
      }

      public static MyVector operator +(MyVector leftVector, MyVector rightVector)
      {
         return new MyVector(leftVector._x + rightVector._x, leftVector._y + rightVector._y);
      }

      public static MyVector operator -(MyVector leftVector, MyVector rightVector)
      {
         return new MyVector(leftVector._x - rightVector._x, leftVector._y - rightVector._y);
      }

      public static MyVector operator *(MyVector aVector, double aScalar)
      {
         return new MyVector(aVector._x * aScalar, aVector._y * aScalar);
      }

      // Added using ReSharper due to CodeAnalysis nagging

      public bool Equals(MyVector other)
      {
         return _x.Equals(other._x) && _y.Equals(other._y);
      }

      public override bool Equals(object obj)
      {
         if (ReferenceEquals(null, obj)) return false;
         return obj is MyVector && Equals((MyVector) obj);
      }

      public override int GetHashCode()
      {
         unchecked
         {
            return (_x.GetHashCode()*397) ^ _y.GetHashCode();
         }
      }

      public static bool operator ==(MyVector left, MyVector right)
      {
         return left.Equals(right);
      }

      public static bool operator !=(MyVector left, MyVector right)
      {
         return !left.Equals(right);
      }
   }
