// find closest point to P on line segment AB:
vec3 closest_point_on_line_segment(in vec3 P, in vec3 A, in vec3 B) {
    vec3 AP = P - A, AB = B - A;
    float l = dot(AB, AB);
    if (l <= 0.0000001) return A;    // A and B are practically the same
    return AP - AB*clamp(dot(AP, AB)/l, 0.0, 1.0);  // do the projection
}
