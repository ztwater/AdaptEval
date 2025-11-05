def pivots_high(data, LBR, LBL):
    pivots = []
    for i in range(len(data)-LBR):
        pivots.append(0)
        pivot = True
        if i > LBL:
            for j in range(LBL + 1):
                if data[i - j] > data[I]:  # do if data[i - j] < data[i] for pivot low
                    pivot = False
            for j in range(LBR + 1):
                if data[i + j] > data[I]:  # do if data[i + j] < data[i] for pivot low
                    pivot = False
        if pivot is True:
            pivots[len(pivots)-1] = data[i]
    for p in range(LBR):
        pivots.append(0)  # This is so the pivots length matches your data length
    return pivots  # The Pivots will be any value that is not 0 and it will be where the lowest/highest value is
