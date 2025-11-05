plDist(x, y, x1, y1, x2, y2) {
    A:= x - x1
    B:= y - y1
    C:= x2 - x1
    D:= y2 - y1

    dot:= A*C + B*D
    sqLen:= C*C + D*D
    param:= dot / sqLen

    if (param < 0 || ((x1 = x2) && (y1 = y2))) {
        xx:= x1
        yy:= y1
    } else if (param > 1) {
        xx:= x2
        yy:= y2
    } else {
        xx:= x1 + param*C
        yy:= y1 + param*D
    }

    dx:= x - xx
    dy:= y - yy

    return sqrt(dx*dx + dy*dy)
}
