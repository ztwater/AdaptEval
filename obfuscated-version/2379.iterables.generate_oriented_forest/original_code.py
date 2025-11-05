def generate_oriented_forest_2(n): 
    """SIAM J. COMPUT. Vol. 9, No. 4, November 1980
    T. Beyer and S.M. Hedetniemi: constant time generation of rooted trees.""" 

    L = range(-1, n) 
    while True: 
        yield L[1:] 
        if L[n] > 0: L[n] = L[L[n]] 
        else:
            for p in range(n-1, 0, -1): 
                if L[p] != 0: break
            else: break
            for q in range(p-1, 0, -1):
                if L[q] == L[p] - 1: break 
            i = p
            while i <= n:
                L[i] = L[i-(p-q)]
                i += 1 
