def reject_outliers(data, m=2):
    stdev = np.std(data)
    mean = np.mean(data)
    maskMin = mean - stdev * m
    maskMax = mean + stdev * m
    mask = np.ma.masked_outside(data, maskMin, maskMax)
    print('Masking values outside of {} and {}'.format(maskMin, maskMax))
    return mask
