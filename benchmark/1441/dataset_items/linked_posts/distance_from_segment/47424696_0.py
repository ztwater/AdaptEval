// line (a -> b ) point p[enter image description here][1]
float distanceToLine(vec2 a, vec2 b, vec2 p) {
    float aside = dot((p - a),(b - a));
    if(aside< 0.0) return length(p-a);
    float bside = dot((p - b),(a - b));
    if(bside< 0.0) return length(p-b);
    vec2 pointOnLine = (bside*a + aside*b)/pow(length(a-b),2.0);
    return length(p - pointOnLine);
}
