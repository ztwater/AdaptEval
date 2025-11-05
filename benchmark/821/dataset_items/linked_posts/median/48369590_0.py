def median(data):
    data.sort()
    mid = len(data) // 2
    return (data[mid] + data[~mid]) / 2.0
