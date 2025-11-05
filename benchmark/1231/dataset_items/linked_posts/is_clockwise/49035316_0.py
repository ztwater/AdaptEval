    for (i, point) in allPoints.enumerated() {
        let nextPoint = i == allPoints.count - 1 ? allPoints[0] : allPoints[i+1]
        signedArea += (point.x * nextPoint.y - nextPoint.x * point.y)
    }

    let clockwise  = signedArea < 0
