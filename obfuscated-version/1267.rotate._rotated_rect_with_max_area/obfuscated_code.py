def rotatedRectWithMaxArea(var_0, var_1, var_2):
  """
  Given a rectangle of size wxh that has been rotated by 'angle' (in
  radians), computes the width and height of the largest possible
  axis-aligned rectangle (maximal area) within the rotated rectangle.
  """
  if var_0 <= 0 or var_1 <= 0:
    return 0,0

  var_3 = var_0 >= var_1
  side_long, side_short = (var_0,var_1) if var_3 else (var_1,var_0)

  # since the solutions for angle, -angle and 180-angle are all the same,
  # if suffices to look at the first quadrant and the absolute values of sin,cos:
  sin_a, cos_a = abs(math.sin(var_2)), abs(math.cos(var_2))
  if side_short <= 2.*sin_a*cos_a*side_long or abs(sin_a-cos_a) < 1e-10:
    # half constrained case: two crop corners touch the longer side,
    #   the other two corners are on the mid-line parallel to the longer line
    var_4 = 0.5*side_short
    wr,hr = (var_4/sin_a,var_4/cos_a) if var_3 else (var_4/cos_a,var_4/sin_a)
  else:
    # fully constrained case: crop touches all 4 sides
    var_5 = cos_a*cos_a - sin_a*sin_a
    wr,hr = (var_0*cos_a - var_1*sin_a)/var_5, (var_1*cos_a - var_0*sin_a)/var_5

  return wr,hr
