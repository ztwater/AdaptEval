public static function segmentDistToPoint(segA:Point, segB:Point, p:Point):Number
{
    var p2:Point = new Point(segB.x - segA.x, segB.y - segA.y);
    var something:Number = p2.x*p2.x + p2.y*p2.y;
    var u:Number = ((p.x - segA.x) * p2.x + (p.y - segA.y) * p2.y) / something;

    if (u > 1)
        u = 1;
    else if (u < 0)
        u = 0;

    var x:Number = segA.x + u * p2.x;
    var y:Number = segA.y + u * p2.y;

    var dx:Number = x - p.x;
    var dy:Number = y - p.y;

    var dist:Number = Math.sqrt(dx*dx + dy*dy);

    return dist;
}
