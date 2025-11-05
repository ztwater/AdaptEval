for i in range(len(b)):
    for k in range(len(b[i])):
        closest = a[0]
        for j in range(1, len(a)):
            if abs(a[j] - b[i][k]) < abs(closest - b[i][k]):
                closest = a[j]
        b[i][k] = closest
