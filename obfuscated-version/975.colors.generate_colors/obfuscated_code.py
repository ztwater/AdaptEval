def rand_cmap(var_0, var_1='bright', var_2=True, var_3=False, var_4=True):
    """
    Creates a random colormap to be used together with matplotlib. Useful for segmentation tasks
    :param nlabels: Number of labels (size of colormap)
    :param type: 'bright' for strong colors, 'soft' for pastel colors
    :param first_color_black: Option to use first color as black, True or False
    :param last_color_black: Option to use last color as black, True or False
    :param verbose: Prints the number of labels and shows the colormap. True or False
    :return: colormap for matplotlib
    """
    from matplotlib.colors import LinearSegmentedColormap
    import colorsys
    import numpy as np


    if var_1 not in ('bright', 'soft'):
        print ('Please choose "bright" or "soft" for type')
        return

    if var_4:
        print('Number of labels: ' + str(var_0))

    # Generate color map for bright colors, based on hsv
    if var_1 == 'bright':
        var_5 = [(np.random.uniform(low=0.0, high=1),
                          np.random.uniform(low=0.2, high=1),
                          np.random.uniform(low=0.9, high=1)) for i in xrange(var_0)]

        # Convert HSV list to RGB
        var_6 = []
        for HSVcolor in var_5:
            var_6.append(colorsys.hsv_to_rgb(HSVcolor[0], HSVcolor[1], HSVcolor[2]))

        if var_2:
            var_6[0] = [0, 0, 0]

        if var_3:
            var_6[-1] = [0, 0, 0]

        var_7 = LinearSegmentedColormap.from_list('new_map', var_6, N=var_0)

    # Generate soft pastel colors, by limiting the RGB spectrum
    if var_1 == 'soft':
        var_8 = 0.6
        var_9 = 0.95
        var_6 = [(np.random.uniform(var_8=var_8, var_9=var_9),
                          np.random.uniform(var_8=var_8, var_9=var_9),
                          np.random.uniform(var_8=var_8, var_9=var_9)) for i in xrange(var_0)]

        if var_2:
            var_6[0] = [0, 0, 0]

        if var_3:
            var_6[-1] = [0, 0, 0]
        var_7 = LinearSegmentedColormap.from_list('new_map', var_6, N=var_0)

    # Display colorbar
    if var_4:
        from matplotlib import colors, colorbar
        from matplotlib import pyplot as plt
        fig, ax = plt.subplots(1, 1, figsize=(15, 0.5))

        var_10 = np.linspace(0, var_0, var_0 + 1)
        var_11 = colors.BoundaryNorm(var_10, var_0)

        var_12 = colorbar.ColorbarBase(ax, cmap=var_7, var_11=var_11, spacing='proportional', ticks=None,
                                   boundaries=var_10, format='%1i', orientation=u'horizontal')

    return var_7
