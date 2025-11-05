#include <math.h>
#define PIV2 M_PI+M_PI
#define C360 360.0000000000000000000
double difangrad(double x, double y)
{
double arg;

arg = fmod(y-x, PIV2);
if (arg < 0 )  arg  = arg + PIV2;
if (arg > M_PI) arg  = arg - PIV2;

return (-arg);
}
double difangdeg(double x, double y)
{
double arg;
arg = fmod(y-x, C360);
if (arg < 0 )  arg  = arg + C360;
if (arg > 180) arg  = arg - C360;
return (-arg);
}
