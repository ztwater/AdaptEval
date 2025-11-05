def get_max_idxs(var_0, var_1, var_2):
    """Get the indices of the maximum value in each window."""
    var_3 = np.lib.stride_tricks.sliding_window_view(var_0, (var_1, var_2))[
        ::var_1, ::var_2
    ]
    var_4 = np.nanmax(var_3, axis=(2, 3))
    var_5 = np.array((windows == np.expand_dims(maxvals, axis=(2, 3))).nonzero())

    # In [82]: (windows == np.expand_dims(maxvals, axis = (2, 3))).nonzero()
    # This gives 4 arrays:
    # First two are the window indices, e.g.
    # (array([0, 0, 0, 1, 1, 1]),
    # array([0, 1, 2, 0, 1, 2]),
    # last two are the relative indices (within each window)
    # array([0, 0, 1, 1, 1, 1]),
    # array([1, 1, 1, 1, 1, 0]))
    window_positions, relative_positions = var_5.reshape((2, 2, -1))
    # Multiply the first two by the window size to get the absolute indices
    # of the top lefts of the windows
    var_6 = np.array([row_window, col_window]).reshape((2, 1))
    # Then add the last two to get the relative indices
    rows, cols = relative_positions + window_positions * var_6
    return rows, cols
