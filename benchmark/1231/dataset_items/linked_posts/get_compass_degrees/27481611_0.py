/**
 * Work out the angle from the x horizontal winding anti-clockwise 
 * in screen space. 
 * 
 * The value returned from the following should be 315. 
 * <pre>
 * x,y -------------
 *     |  1,1
 *     |    \
 *     |     \
 *     |     2,2
 * </pre>
 * @param p1
 * @param p2
 * @return - a double from 0 to 360
 */
public static double angleOf(PointF p1, PointF p2) {
    // NOTE: Remember that most math has the Y axis as positive above the X.
    // However, for screens we have Y as positive below. For this reason, 
    // the Y values are inverted to get the expected results.
    final double deltaY = (p1.y - p2.y);
    final double deltaX = (p2.x - p1.x);
    final double result = Math.toDegrees(Math.atan2(deltaY, deltaX)); 
    return (result < 0) ? (360d + result) : result;
}
