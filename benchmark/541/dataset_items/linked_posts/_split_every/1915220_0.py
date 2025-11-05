def splitEveryN(n, it):
    return [it[i:i+n] for i in range(0, len(it), n)]
