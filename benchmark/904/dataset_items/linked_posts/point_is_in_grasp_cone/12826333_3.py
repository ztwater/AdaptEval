orth_distance = length((p - x) - cone_dist * dir)

is_point_inside_cone = (orth_distance < cone_radius)
