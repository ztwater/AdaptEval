"""
This module provides various methods to handle geometric problems.
"""
from typing import List

import numpy as np

def is_clockwise(polyline: List[np.ndarray]):
    """
    determines if points in a polyline are ordered clockwise or anti-clockwise.
    If result > 0, points are orderered clockwise.
    If result < 0, points are ordered anti_clockwise.
    If result = 0, we have a straight line.

    Source: https://stackoverflow.com/a/61991493/13700747

    :param polyline: a polyline
    :type polyline: List[np.ndarray]
    :return: s
    :rtype: float
    """

    assert len(polyline) > 0
    s = 0.0
    for p1, p2 in zip(polyline, polyline[1:] + [polyline[0]]):
        s += (p2[0] - p1[0]) * (p2[1] + p1[1])
    return s
