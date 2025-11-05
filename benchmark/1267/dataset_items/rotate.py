import math


def _rotated_rect_with_max_area(h, w, angle):
        """
        Given a rectangle of size wxh that has been rotated by 'angle' (in
        degrees), computes the width and height of the largest possible
        axis-aligned rectangle (maximal area) within the rotated rectangle.

        Code from: https://stackoverflow.com/questions/16702966/rotate-image-and-crop-out-black-borders
        """

        angle = math.radians(angle)
        width_is_longer = w >= h
        side_long, side_short = (w, h) if width_is_longer else (h, w)

        # since the solutions for angle, -angle and 180-angle are all the same,
        # it is sufficient to look at the first quadrant and the absolute values of sin,cos:
        sin_a, cos_a = abs(math.sin(angle)), abs(math.cos(angle))
        if side_short <= 2.0 * sin_a * cos_a * side_long or abs(sin_a - cos_a) < 1e-10:
            # half constrained case: two crop corners touch the longer side,
            # the other two corners are on the mid-line parallel to the longer line
            x = 0.5 * side_short
            wr, hr = (x / sin_a, x / cos_a) if width_is_longer else (x / cos_a, x / sin_a)
        else:
            # fully constrained case: crop touches all 4 sides
            cos_2a = cos_a * cos_a - sin_a * sin_a
            wr, hr = (w * cos_a - h * sin_a) / cos_2a, (h * cos_a - w * sin_a) / cos_2a

        return dict(
            x_min=max(0, int(w / 2 - wr / 2)),
            x_max=min(w, int(w / 2 + wr / 2)),
            y_min=max(0, int(h / 2 - hr / 2)),
            y_max=min(h, int(h / 2 + hr / 2)),
        )
