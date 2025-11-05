distToSegment: function (point, linePointA, linePointB){

    var x0 = point.X;
    var y0 = point.Y;

    var x1 = linePointA.X;
    var y1 = linePointA.Y;

    var x2 = linePointB.X;
    var y2 = linePointB.Y;

    var Dx = (x2 - x1);
    var Dy = (y2 - y1);

    var numerator = Math.abs(Dy*x0 - Dx*y0 - x1*y2 + x2*y1);
    var denominator = Math.sqrt(Dx*Dx + Dy*Dy);
    if (denominator == 0) {
        return this.dist2(point, linePointA);
    }

    return numerator/denominator;

}
