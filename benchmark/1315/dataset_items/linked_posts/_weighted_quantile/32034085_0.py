def weighted_percentile(a, percentile = np.array([75, 25]), weights=None):
    """
    O(nlgn) implementation for weighted_percentile.
    """
    percentile = np.array(percentile)/100.0
    if weights is None:
        weights = np.ones(len(a))
    a_indsort = np.argsort(a)
    a_sort = a[a_indsort]
    weights_sort = weights[a_indsort]
    ecdf = np.cumsum(weights_sort)

    percentile_index_positions = percentile * (weights.sum()-1)+1
    # need the 1 offset at the end due to ecdf not starting at 0
    locations = np.searchsorted(ecdf, percentile_index_positions)

    out_percentiles = np.zeros(len(percentile_index_positions))

    for i, empiricalLocation in enumerate(locations):
        # iterate across the requested percentiles 
        if ecdf[empiricalLocation-1] == np.floor(percentile_index_positions[i]):
            # i.e. is the percentile in between 2 separate values
            uppWeight = percentile_index_positions[i] - ecdf[empiricalLocation-1]
            lowWeight = 1 - uppWeight

            out_percentiles[i] = a_sort[empiricalLocation-1] * lowWeight + \
                                 a_sort[empiricalLocation] * uppWeight
        else:
            # i.e. the percentile is entirely in one bin
            out_percentiles[i] = a_sort[empiricalLocation]

    return out_percentiles
