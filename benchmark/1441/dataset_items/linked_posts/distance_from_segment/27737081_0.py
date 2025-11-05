    /* Distance from a point (p1) to line l1 l2 */
func distanceFromPoint(p: CGPoint, toLineSegment l1: CGPoint, and l2: CGPoint) -> CGFloat {
    let A = p.x - l1.x
    let B = p.y - l1.y
    let C = l2.x - l1.x
    let D = l2.y - l1.y
    
    let dot = A * C + B * D
    let len_sq = C * C + D * D
    var param : CGFloat = -1
    if len_sq != 0 {
        param = dot / len_sq
    }
    
    var xx, yy: CGFloat
    
    if param < 0 || (l1.x == l2.x && l1.y == l2.y) {
        xx = l1.x
        yy = l1.y
    } else if param > 1 {
        xx = l2.x
        yy = l2.y
    } else {
        xx = l1.x + param * C
        yy = l1.y + param * D
    }
    
    let dx = p.x - xx
    let dy = p.y - yy
    
    return sqrt(dx * dx + dy * dy)
}
