from __future__ import annotations

from typing import TYPE_CHECKING, Any, Union

import numpy as np

if TYPE_CHECKING:
    from numpy.typing import NDArray

def get_closest(sorted_array: NDArray, values: NDArray) -> NDArray:
    """Fast way to find the nearest element in 'sorted_array' for each element in 'values'.

    Solution taken from https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array/46184652#46184652.

    Args:
        sorted_array: a sorted array
        values: an array of arbitrary values

    Returns:
        for each element in the 'values' array the closest element in 'sorted_array' is returned
    """
    # sorted_array = np.array(sorted_array)
    # get insert positions
    idxs = np.searchsorted(sorted_array, values, side="left")

    # find indexes where previous index is closer
    prev_idx_is_less = (idxs == len(sorted_array)) | (
        np.fabs(values - sorted_array[np.maximum(idxs - 1, 0)])
        < np.fabs(values - sorted_array[np.minimum(idxs, len(sorted_array) - 1)])
    )
    idxs[prev_idx_is_less] -= 1

    return sorted_array[idxs]

