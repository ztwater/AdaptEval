fun calculateAngle(
    touchX: Float,
    touchY: Float,
    centerX: Float,
    centerY: Float
): Float {
    val deltaX = centerX - touchX
    val deltaY = centerY - touchY
    return Math.toDegrees(atan2(deltaY.toDouble(), deltaX.toDouble())).toFloat()
}
