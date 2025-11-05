d = defaultdict(int)
for x in stuff:
    d[x.a,x.b] += x.c_int
    # ^^^^^^^ tuple key
