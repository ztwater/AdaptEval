inline double getAbsoluteDiff2Angles(const double x, const double y, const double c)
{
    // c can be PI (for radians) or 180.0 (for degrees);
    return c - fabs(fmod(fabs(x - y), 2*c) - c);
}
