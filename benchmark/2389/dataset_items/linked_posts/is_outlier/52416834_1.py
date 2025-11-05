def sd_outlier(x, axis = None, bar = 3, side = 'both'):
    assert side in ['gt', 'lt', 'both'], 'Side should be `gt`, `lt` or `both`.'

    d_z = stat.zscore(x, axis = axis)

    if side == 'gt':
        return d_z > bar
    elif side == 'lt':
        return d_z < -bar
    elif side == 'both':
        return np.abs(d_z) > bar
