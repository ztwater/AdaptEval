fun getDistance(x: Double, y: Double, x1: Double, y1: Double, x2: Double, y2: Double): Double {
    val a = x - x1
    val b = y - y1
    val c = x2 - x1
    val d = y2 - y1

    val lenSq = c * c + d * d
    val param = if (lenSq != .0) { //in case of 0 length line
        val dot = a * c + b * d
        dot / lenSq
    } else {
        -1.0
    }

    val (xx, yy) = when {
        param < 0 -> x1 to y1
        param > 1 -> x2 to y2
        else -> x1 + param * c to y1 + param * d
    }

    val dx = x - xx
    val dy = y - yy
    return hypot(dx, dy)
}
