/**
 * Static util function to determine is a point(px,py) on the line(x1,y1,x2,y2)
 * A simple hit test.
 * 
 * @return {boolean}
 * @static
 * @private
 * @param {Number} coronaWidth the accepted corona for the hit test
 * @param {Number} X1 x coordinate of the start point of the line
 * @param {Number} Y1 y coordinate of the start point of the line
 * @param {Number} X2 x coordinate of the end point of the line
 * @param {Number} Y2 y coordinate of the end point of the line
 * @param {Number} px x coordinate of the point to test
 * @param {Number} py y coordinate of the point to test
 **/
graphiti.shape.basic.Line.hit= function( coronaWidth, X1, Y1,  X2,  Y2, px, py)
{
  // Adjust vectors relative to X1,Y1
  // X2,Y2 becomes relative vector from X1,Y1 to end of segment
  X2 -= X1;
  Y2 -= Y1;
  // px,py becomes relative vector from X1,Y1 to test point
  px -= X1;
  py -= Y1;
  var dotprod = px * X2 + py * Y2;
  var projlenSq;
  if (dotprod <= 0.0) {
      // px,py is on the side of X1,Y1 away from X2,Y2
      // distance to segment is length of px,py vector
      // "length of its (clipped) projection" is now 0.0
      projlenSq = 0.0;
  } else {
      // switch to backwards vectors relative to X2,Y2
      // X2,Y2 are already the negative of X1,Y1=>X2,Y2
      // to get px,py to be the negative of px,py=>X2,Y2
      // the dot product of two negated vectors is the same
      // as the dot product of the two normal vectors
      px = X2 - px;
      py = Y2 - py;
      dotprod = px * X2 + py * Y2;
      if (dotprod <= 0.0) {
          // px,py is on the side of X2,Y2 away from X1,Y1
          // distance to segment is length of (backwards) px,py vector
          // "length of its (clipped) projection" is now 0.0
          projlenSq = 0.0;
      } else {
          // px,py is between X1,Y1 and X2,Y2
          // dotprod is the length of the px,py vector
          // projected on the X2,Y2=>X1,Y1 vector times the
          // length of the X2,Y2=>X1,Y1 vector
          projlenSq = dotprod * dotprod / (X2 * X2 + Y2 * Y2);
      }
  }
    // Distance to line is now the length of the relative point
    // vector minus the length of its projection onto the line
    // (which is zero if the projection falls outside the range
    //  of the line segment).
    var lenSq = px * px + py * py - projlenSq;
    if (lenSq < 0) {
        lenSq = 0;
    }
    return Math.sqrt(lenSq)<coronaWidth;
};
