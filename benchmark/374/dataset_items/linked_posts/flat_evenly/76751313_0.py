tree = [[1, 2, 3],
        [4, 5],
        [6, 8, 9, 10],
        [11]]

stump = [
    sublist[i]
    for i in range(max(map(len, tree)))
    for sublist in tree if len(sublist) > i
    ]

print(stump) #[1, 4, 6, 11, 2, 5, 8, 3, 9, 10]
