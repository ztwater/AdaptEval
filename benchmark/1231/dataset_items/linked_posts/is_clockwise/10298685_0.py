signedArea = 0
for each point in points:
    x1 = point[0]
    y1 = point[1]
    if point is last point
        x2 = firstPoint[0]
        y2 = firstPoint[1]
    else
        x2 = nextPoint[0]
        y2 = nextPoint[1]
    end if

    signedArea += (x1 * y2 - x2 * y1)
end for
return signedArea / 2
