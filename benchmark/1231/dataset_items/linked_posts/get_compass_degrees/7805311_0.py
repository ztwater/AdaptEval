/**
 * Fetches angle relative to screen centre point
 * where 3 O'Clock is 0 and 12 O'Clock is 270 degrees
 * 
 * @param screenPoint
 * @return angle in degress from 0-360.
 */
public double getAngle(Point screenPoint) {
    double dx = screenPoint.getX() - mCentreX;
    // Minus to correct for coord re-mapping
    double dy = -(screenPoint.getY() - mCentreY);

    double inRads = Math.atan2(dy, dx);

    // We need to map to coord system when 0 degree is at 3 O'clock, 270 at 12 O'clock
    if (inRads < 0)
        inRads = Math.abs(inRads);
    else
        inRads = 2 * Math.PI - inRads;

    return Math.toDegrees(inRads);
}
