   public static class JustTesting
   {
      public static void Main()
      {
         Stopwatch stopwatch = new Stopwatch();
         stopwatch.Start();

         for (int i = 0; i < 10000000; i++)
         {
            TestIt(1, 0, 0, 0, 1, 1, 0.70710678118654757);
            TestIt(5, 4, 0, 0, 20, 10, 1.3416407864998738);
            TestIt(30, 15, 0, 0, 20, 10, 11.180339887498949);
            TestIt(-30, 15, 0, 0, 20, 10, 33.541019662496844);
            TestIt(5, 1, 0, 0, 10, 0, 1.0);
            TestIt(1, 5, 0, 0, 0, 10, 1.0);
         }

         stopwatch.Stop();
         TimeSpan timeSpan = stopwatch.Elapsed;
      }


      private static void TestIt(float aPointX, float aPointY, 
                                 float lineSegmentPoint1X, float lineSegmentPoint1Y, 
                                 float lineSegmentPoint2X, float lineSegmentPoint2Y, 
                                 double expectedAnswer)
      {
         // Katz
         double d1 = DistanceFromPointToLineSegment(new MyVector(aPointX, aPointY), 
                                              new MyVector(lineSegmentPoint1X, lineSegmentPoint1Y), 
                                              new MyVector(lineSegmentPoint2X, lineSegmentPoint2Y));
         Debug.Assert(d1 == expectedAnswer);

         /*
         // Katz using squared distance
         double d2 = DistanceFromPointToLineSegmentSquared(new MyVector(aPointX, aPointY), 
                                              new MyVector(lineSegmentPoint1X, lineSegmentPoint1Y), 
                                              new MyVector(lineSegmentPoint2X, lineSegmentPoint2Y));
         Debug.Assert(Math.Abs(d2 - expectedAnswer * expectedAnswer) < 1E-7f);
          */

         /*
         // Matti (optimized)
         double d3 = FloatVector.DistanceToLineSegment(new PointF(aPointX, aPointY), 
                                                new PointF(lineSegmentPoint1X, lineSegmentPoint1Y), 
                                                new PointF(lineSegmentPoint2X, lineSegmentPoint2Y));
         Debug.Assert(Math.Abs(d3 - expectedAnswer) < 1E-7f);
          */
      }

      private static double DistanceFromPointToLineSegment(MyVector aPoint, 
                                             MyVector lineSegmentPoint1, MyVector lineSegmentPoint2)
      {
         MyVector closestPoint;  // Not used
         return aPoint.DistanceToLineSegment(lineSegmentPoint1, lineSegmentPoint2, 
                                             out closestPoint);
      }

      private static double DistanceFromPointToLineSegmentSquared(MyVector aPoint, 
                                             MyVector lineSegmentPoint1, MyVector lineSegmentPoint2)
      {
         MyVector closestPoint;  // Not used
         return aPoint.DistanceToLineSegmentSquared(lineSegmentPoint1, lineSegmentPoint2, 
                                                    out closestPoint);
      }
   }
