def generate_oriented_forest(n):
    """Algorithm O from Knuth TAoCP, Fascicle 4, p. 25. """
    p = range(-1,n)
    while True:
        yield p[1:]
        if p[n] > 0:
            p[n] = p[p[n]]
            continue
        for k in range(n-1,0,-1):
            if p[k] != 0: break
        else:
            break
        j = p[k]
        d = k-j
        while True:
            if p[k-d] == p[j]:
                p[k] = p[j]
            else:
                p[k] = p[k-d] + d
            if k==n:
                break
            k+=1

if __name__ == "__main__":
    for el in generate_oriented_forest(4):
        print el
