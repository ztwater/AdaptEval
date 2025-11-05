//st = start of line segment
//b = the line segment (as in: st + b = end of line segment)
//pt = point to test
//Returns distance from point to line segment.  
//Note: nearest point on the segment to the test point is right there if we ever need it
public static function linePointDist( st:Point, b:Point, pt:Point ):Number
{
    var nearestPt:Point; //closest point on seqment to pt

    var keyDot:Number = dot( b, pt.subtract( st ) ); //key dot product
    var bLenSq:Number = dot( b, b ); //Segment length squared

    if( keyDot <= 0 )  //pt is "behind" st, use st
    {
        nearestPt = st  
    }
    else if( keyDot >= bLenSq ) //pt is "past" end of segment, use end (notice we are saving twin sqrts here cuz)
    {
        nearestPt = st.add(b);
    }
    else //pt is inside segment, reuse keyDot and bLenSq to get percent of seqment to move in to find closest point
    {
        var keyDotToPctOfB:Number = keyDot/bLenSq; //REM dot product comes squared
        var partOfB:Point = new Point( b.x * keyDotToPctOfB, b.y * keyDotToPctOfB );
        nearestPt = st.add(partOfB);
    }

    var dist:Number = (pt.subtract(nearestPt)).length;

    return dist;
}
