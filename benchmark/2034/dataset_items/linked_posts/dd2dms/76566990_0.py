def to_dms(decimal_degrees):
    # convert degrees into dms and a sign indicator
    degrees = np.array(decimal_degrees)
    sign = np.where(degrees < 0, -1, 1)
    r, s = np.divmod(np.round(np.abs(degrees) * 3600, 1), 60)
    d, m = np.divmod(r, 60)
    # np.transpose([d, m, s]*sign)  # if you wanted signed results
    return np.transpose([d, m, s, sign])

# print("array test:", to_dms([101.816652, -101.816653]))
# array test: [[101. 48. 59.9000000000232831 1.] [101. 49. 0. -1.]]
