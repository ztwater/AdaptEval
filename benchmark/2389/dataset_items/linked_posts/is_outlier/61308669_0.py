def reject_outliers(data, m = 2.):
        d = np.abs(data - np.median(data))
        mdev = np.median(d)
        s = d/mdev if mdev else 0.
        data_range = np.arange(len(data))
        idx_list = data_range[s>=m]
        return data[s<m], idx_list

data_points = np.array([8, 10, 35, 17, 73, 77])  
print(reject_outliers(data_points))

after rejection: [ 8 10 35 17], index positions of outliers: [4 5]
