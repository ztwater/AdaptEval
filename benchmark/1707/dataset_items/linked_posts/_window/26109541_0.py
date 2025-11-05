def rolling_window(list, degree):
    for i in range(len(list)-degree+1):
        yield [list[i+o] for o in range(degree)]
