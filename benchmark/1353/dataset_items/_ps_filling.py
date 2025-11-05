import numpy as np
 
def _get_max_idxs(arr, row_looks, col_looks):
    """Get the indices of the maximum value in each look window."""
    if row_looks == 1 and col_looks == 1:
        # No need to pad if we're not looking
        return np.where(arr == arr)
    # Adjusted from this answer to not take every moving window
    # https://stackoverflow.com/a/72742009/4174466
    windows = np.lib.stride_tricks.sliding_window_view(arr, (row_looks, col_looks))[
        ::row_looks, ::col_looks
    ]
    maxvals = np.nanmax(windows, axis=(2, 3))
    indx = np.array((windows == np.expand_dims(maxvals, axis=(2, 3))).nonzero())

    # In [82]: (windows == np.expand_dims(maxvals, axis = (2, 3))).nonzero()
    # This gives 4 arrays:
    # First two are the window indices
    # (array([0, 0, 0, 1, 1, 1]),
    # array([0, 1, 2, 0, 1, 2]),
    # last two are the relative indices (within each window)
    # array([0, 0, 1, 1, 1, 1]),
    # array([1, 1, 1, 1, 1, 0]))
    window_positions, relative_positions = indx.reshape((2, 2, -1))
    # Multiply the first two by the window size to get the absolute indices
    # of the top lefts of the windows
    window_offsets = np.array([row_looks, col_looks]).reshape((2, 1))
    # Then add the last two to get the relative indices
    rows, cols = relative_positions + window_positions * window_offsets
    return rows, cols
