def adjust_lightness(var_0, var_1=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        var_2 = mc.cnames[var_0]
    except:
        var_2 = var_0
    var_2 = colorsys.rgb_to_hls(*mc.to_rgb(var_2))
    return colorsys.hls_to_rgb(var_2[0], max(0, min(1, var_1 * var_2[1])), var_2[2])
