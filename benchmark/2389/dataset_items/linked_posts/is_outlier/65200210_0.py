def outlier_smoother(x, m=3, win=3, plots=False):
    ''' finds outliers in x, points > m*mdev(x) [mdev:median deviation] 
    and replaces them with the median of win points around them '''
    x_corr = np.copy(x)
    d = np.abs(x - np.median(x))
    mdev = np.median(d)
    idxs_outliers = np.nonzero(d > m*mdev)[0]
    for i in idxs_outliers:
        if i-win < 0:
            x_corr[i] = np.median(np.append(x[0:i], x[i+1:i+win+1]))
        elif i+win+1 > len(x):
            x_corr[i] = np.median(np.append(x[i-win:i], x[i+1:len(x)]))
        else:
            x_corr[i] = np.median(np.append(x[i-win:i], x[i+1:i+win+1]))
    if plots:
        plt.figure('outlier_smoother', clear=True)
        plt.plot(x, label='orig.', lw=5)
        plt.plot(idxs_outliers, x[idxs_outliers], 'ro', label='outliers')                                                                                                                    
        plt.plot(x_corr, '-o', label='corrected')
        plt.legend()
    
    return x_corr
