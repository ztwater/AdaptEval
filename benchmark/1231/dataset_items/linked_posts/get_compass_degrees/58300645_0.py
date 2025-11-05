private fun angleBetweenPoints(a: PointF, b: PointF): Double {
        val deltaY = abs(b.y - a.y)
        val deltaX = abs(b.x - a.x)
        return Math.toDegrees(atan2(deltaY.toDouble(), deltaX.toDouble()))
    }
