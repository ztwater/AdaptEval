double k1 = cameraIntrinsic.distortion[0];
double k2 = cameraIntrinsic.distortion[1];
double p1 = cameraIntrinsic.distortion[2];
double p2 = cameraIntrinsic.distortion[3];
double k3 = cameraIntrinsic.distortion[4];
double fu = cameraIntrinsic.focalLength[0];
double fv = cameraIntrinsic.focalLength[1];
double u0 = cameraIntrinsic.principalPoint[0];
double v0 = cameraIntrinsic.principalPoint[1];
double u, v;


u = thisPoint->x; // the undistorted point
v = thisPoint->y;
double x = ( u - u0 )/fu;
double y = ( v - v0 )/fv;

double r2 = (x*x) + (y*y);
double r4 = r2*r2;

double cDist = 1 + (k1*r2) + (k2*r4);
double xr = x*cDist;
double yr = y*cDist;

double a1 = 2*x*y;
double a2 = r2 + (2*(x*x));
double a3 = r2 + (2*(y*y));

double dx = (a1*p1) + (a2*p2);
double dy = (a3*p1) + (a1*p2);

double xd = xr + dx;
double yd = yr + dy;

double ud = (xd*fu) + u0;
double vd = (yd*fv) + v0;

thisPoint->x = ud; // the distorted point
thisPoint->y = vd;
