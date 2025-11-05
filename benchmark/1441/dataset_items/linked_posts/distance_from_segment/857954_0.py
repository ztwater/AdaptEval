// a, b, and c in the code below are all points

function distance(a, b)
{
    var dx = a.x - b.x;
    var dy = a.y - b.y;
    return Math.sqrt(dx*dx + dy*dy);
}

function Segment(a, b)
{
    var ab = {
        x: b.x - a.x,
        y: b.y - a.y
    };
    var length = distance(a, b);

    function cross(c) {
        return ab.x * (c.y-a.y) - ab.y * (c.x-a.x);
    };

    this.distanceFrom = function(c) {
        return Math.min(distance(a,c),
                        distance(b,c),
                        Math.abs(cross(c) / length));
    };
}
