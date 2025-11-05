// find closest point to P on line segment AB:
vec3 closest_point_on_line_segment(in vec3 P, in vec3 A, in vec3 B) {
    vec3 AP = P - A, AB = B - A;
    return AP - AB*clamp(dot(AP, AB)/dot(AB, AB), 0.0, 1.0);
}
