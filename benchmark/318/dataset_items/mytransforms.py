import math


class RandomRotate(object):
    """ Rotates the image randomly in a specified angular range

    This transform will rotate the image in a given range. Afterwards, a center crop is performed to ensure that
    there is no boundary with invalid values. The crop size is always determined beased on the largest possible
    rotation.
    """

    def __init__(self, rotation, fraction=1.0):
        """ Creates a RandomRotate object

        :param rotation: defines the rotation angle in degrees. Can be float or 2-tuple with lower and upper boundary
        :param fraction: defines which fraction of images is supposed to be randomly rotated
        """
        assert isinstance(rotation, (float, tuple)), 'rotation has to be a float or a tuple'
        assert isinstance(fraction, float), 'fraction has to be a float'
        assert fraction >= 0 and fraction <= 1, 'fraction has to be between 0 and 1'
        if isinstance(rotation, float):
            self.rotation = (-rotation, rotation)
        else:
            self.rotation = rotation
        self.fraction = fraction

    def _getCropSize(self, w, h, angle):
        """
        Given a rectangle of size w x h that has been rotated by 'angle' (in degrees), computes the width and height of
        the largest possible axis-aligned rectangle (maximal area) within the rotated rectangle.

        This solution is taken from the StackOverflow user coproc: https://stackoverflow.com/a/16778797
        """
        angle = angle * math.pi / 180
        width_is_longer = w >= h
        side_long, side_short = (w, h) if width_is_longer else (h, w)

        # since the solutions for angle, -angle and 180-angle are all the same,
        # if suffices to look at the first quadrant and the absolute values of sin,cos:
        sin_a, cos_a = abs(math.sin(angle)), abs(math.cos(angle))
        if side_short <= 2. * sin_a * cos_a * side_long or abs(sin_a - cos_a) < 1e-10:
            # half constrained case: two crop corners touch the longer side,
            #   the other two corners are on the mid-line parallel to the longer line
            x = 0.5 * side_short
            wr, hr = (x / sin_a, x / cos_a) if width_is_longer else (x / cos_a, x / sin_a)
        else:
            # fully constrained case: crop touches all 4 sides
            cos_2a = cos_a * cos_a - sin_a * sin_a
            wr, hr = (w * cos_a - h * sin_a) / cos_2a, (h * cos_a - w * sin_a) / cos_2a
        return hr, wr

    def __eq__(self, other):
        return type(self).__name__ == other.__name__

