def remove_percentile_outliers(data, percent_to_drop=0.001):
    low, high = data.quantile([percent_to_drop / 2, 1-percent_to_drop / 2])
    return data[(data >= low )&(data <= high)]
