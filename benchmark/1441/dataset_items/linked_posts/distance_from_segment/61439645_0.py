    static func magnitude(p1: CGPoint, p2: CGPoint) -> CGFloat {
        let vector = CGPoint(x: p2.x - p1.x, y: p2.y - p1.y)
        return sqrt(pow(vector.x, 2) + pow(vector.y, 2))
    }

    /// http://paulbourke.net/geometry/pointlineplane/
    /// http://paulbourke.net/geometry/pointlineplane/source.c
    static func pointDistanceToLine(point: CGPoint, lineStart: CGPoint, lineEnd: CGPoint) -> CGFloat? {

        let lineMag = magnitude(p1: lineEnd, p2: lineStart)
        let u = (((point.x - lineStart.x) * (lineEnd.x - lineStart.x)) +
                ((point.y - lineStart.y) * (lineEnd.y - lineStart.y))) /
                (lineMag * lineMag)

        if u < 0 || u > 1 {
            // closest point does not fall within the line segment
            return nil
        }

        let intersectionX = lineStart.x + u * (lineEnd.x - lineStart.x)
        let intersectionY = lineStart.y + u * (lineEnd.y - lineStart.y)

        return magnitude(p1: point, p2: CGPoint(x: intersectionX, y: intersectionY))
    }
