test_data = [2,4,5,1,6,5,40, 3]
def reject_outliers(data, m=2):
    mean = np.mean(data)
    std = np.std(data)
    for i in range(len(data)) :
        if np.abs(data[i] -mean) > m*std :
            data[i] = data[i-1]
    return data
reject_outliers(test_data)
