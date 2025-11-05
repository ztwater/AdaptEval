def devideChunks(x, n):
    newList = []
    for i in range(0, len(x), n):
        newList.append(x[i:i + n])

    print(newList)
