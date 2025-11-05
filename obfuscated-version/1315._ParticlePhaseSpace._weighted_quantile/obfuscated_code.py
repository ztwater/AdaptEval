def weighted_quantile(var_0, var_1, var_2=None, 
                      var_3=False, var_4=False):
    """ Very close to numpy.percentile, but supports weights.
    NOTE: quantiles should be in [0, 1]!
    :param values: numpy.array with data
    :param quantiles: array-like with many quantiles needed
    :param sample_weight: array-like of the same length as `array`
    :param values_sorted: bool, if True, then will avoid sorting of
        initial array
    :param old_style: if True, will correct output to be consistent
        with numpy.percentile.
    :return: numpy.array with computed quantiles.
    """
    var_0 = np.array(var_0)
    var_1 = np.array(var_1)
    if var_2 is None:
        var_2 = np.ones(len(var_0))
    var_2 = np.array(var_2)
    assert np.all(var_1 >= 0) and np.all(var_1 <= 1), 'quantiles should be in [0, 1]'

    if not var_3:
        var_5 = np.argsort(var_0)
        var_0 = var_0[var_5]
        var_2 = var_2[var_5]

    var_6 = np.cumsum(var_2) - 0.5 * var_2
    if var_4:
        # To be convenient with numpy.percentile
        var_6 -= var_6[0]
        var_6 /= var_6[-1]
    else:
        var_6 /= np.sum(var_2)
    return np.interp(var_1, var_6, var_0)
