// Given a rectangle of size.width x size.height that has been rotated by 'angle' (in
// radians), computes the width and height of the largest possible
// axis-aligned rectangle (maximal area) within the rotated rectangle.
func rotatedRectWithMaxArea(size: CGSize, angle: CGFloat) -> CGSize {
    let w = size.width
    let h = size.height

    if(w <= 0 || h <= 0) {
        return CGSize.zero
    }

    let widthIsLonger = w >= h
    let (sideLong, sideShort) = widthIsLonger ? (w, h) : (w, h)

    // since the solutions for angle, -angle and 180-angle are all the same,
    // if suffices to look at the first quadrant and the absolute values of sin,cos:
    let (sinA, cosA) = (sin(angle), cos(angle))
    if(sideShort <= 2*sinA*cosA*sideLong || abs(sinA-cosA) < 1e-10) {
        // half constrained case: two crop corners touch the longer side,
        // the other two corners are on the mid-line parallel to the longer line
        let x = 0.5*sideShort
        let (wr, hr) = widthIsLonger ? (x/sinA, x/cosA) : (x/cosA, x/sinA)
        return CGSize(width: wr, height: hr)
    } else {
        // fully constrained case: crop touches all 4 sides
        let cos2A = cosA*cosA - sinA*sinA
        let (wr, hr) = ((w*cosA - h*sinA)/cos2A, (h*cosA - w*sinA)/cos2A)
        return CGSize(width: wr, height: hr)
    }
}
