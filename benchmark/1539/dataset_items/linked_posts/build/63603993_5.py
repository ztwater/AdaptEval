t = [1,0,0,0,0]; [sum( [t[x] for x in xs] ) / len(xs) for xs in kernel_indexes(5,3)]
# => [0.5,0.0,0.0]
