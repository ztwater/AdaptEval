def chunkList(initialList, chunkSize):
    """
    This function chunks a list into sub lists 
    that have a length equals to chunkSize.

    Example:
    lst = [3, 4, 9, 7, 1, 1, 2, 3]
    print(chunkList(lst, 3)) 
    returns
    [[3, 4, 9], [7, 1, 1], [2, 3]]
    """
    finalList = []
    for i in range(0, len(initialList), chunkSize):
        finalList.append(initialList[i:i+chunkSize])
    return finalList
