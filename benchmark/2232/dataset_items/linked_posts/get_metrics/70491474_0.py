uncorrelated_features = features.copy()

# Loop until there's nothing to drop
while True:
    # Calculating the correlation matrix for the remaining list of features
    cor = uncorrelated_features.corr().abs()

    # Generating a square matrix with all 1s except for the main axis
    zero_main = np.triu(np.ones(cor.shape), k=1) +
        np.tril(np.ones(cor.shape), k=-1)

    # Using the zero_main matrix to filter out the main axis of the correlation matrix
    except_main = cor.where(zero_main.astype(bool))

    # Calculating some metrics for each column, including the max correlation,
    # mean correlation and the name of the column
    mertics = [(except_main[column].max(), except_main[column].mean(), column) for column in except_main.columns]

    # Sort the list to find the most suitable candidate to drop at index 0
    mertics.sort(key=lambda x: (x[0], x[1]), reverse=True)

    # Check and see if there's anything to drop from the list of features
    if mertics[0][0] > 0.5:
        uncorrelated_features.drop(mertics[0][2], axis=1, inplace=True)
    else:
        break
