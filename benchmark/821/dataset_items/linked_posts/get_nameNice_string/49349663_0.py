# Copy and paste your camel case code in the string below
camelCaseCode ="""
    cv2.Matx33d ComputeZoomMatrix(const cv2.Point2d & zoomCenter, double zoomRatio)
    {
      auto mat = cv2.Matx33d::eye();
      mat(0, 0) = zoomRatio;
      mat(1, 1) = zoomRatio;
      mat(0, 2) = zoomCenter.x * (1. - zoomRatio);
      mat(1, 2) = zoomCenter.y * (1. - zoomRatio);
      return mat;
    }
"""

import re
def snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def lines(str):
    return str.split("\n")

def unlines(lst):
    return "\n".join(lst)

def words(str):
    return str.split(" ")

def unwords(lst):
    return " ".join(lst)

def map_partial(function):
    return lambda values : [  function(v) for v in values]

import functools
def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

snake_case_code = compose(
    unlines ,
    map_partial(unwords),
    map_partial(map_partial(snake_case)),
    map_partial(words),
    lines
)
print(snake_case_code(camelCaseCode))
