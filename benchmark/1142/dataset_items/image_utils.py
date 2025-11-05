# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import math
from typing import Tuple



def rotate_pixel_coords(origin: Tuple[int, int], point: Tuple[int, int], angle: float) -> Tuple[int, int]:
    """
    Rotate a pixel-index counterclockwise by a given angle around a given origin.
    The angle should be given in radians.

    modified from answer here: https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return int(qx), int(qy)
