def uncorrelated_features(df, threshold=0.7):
    """
    Returns a subset of df columns with Pearson correlations
    below threshold.
    """

    corr = df.corr().abs()
    keep = []
    for i in range(len(corr.iloc[:,0])):
        above = corr.iloc[:i,i]
        if len(keep) > 0: above = above[keep]
        if len(above[above < threshold]) == len(above):
            keep.append(corr.columns.values[i])

    return df[keep]
