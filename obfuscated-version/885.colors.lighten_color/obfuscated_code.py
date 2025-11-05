def lighten_color(var_0, var_1=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        var_2 = mc.cnames[var_0]
    except:
        var_2 = var_0
    var_2 = colorsys.rgb_to_hls(*mc.to_rgb(var_2))
    return colorsys.hls_to_rgb(var_2[0], 1 - var_1 * (1 - var_2[1]), var_2[2])
