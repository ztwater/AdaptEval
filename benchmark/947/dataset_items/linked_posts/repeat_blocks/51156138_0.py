# Get repeats for each group using group lengths/sizes
r1 = np.repeat(np.arange(len(sizes)), repeats)

# Get total size of output array, as needed to initialize output indexing array
N = (sizes*repeats).sum() # or np.dot(sizes, repeats)

# Initialize indexing array with ones as we need to setup incremental indexing
# within each group when cumulatively summed at the final stage. 
# Two steps here:
# 1. Within each group, we have multiple sequences, so setup the offsetting
# at each sequence lengths by the seq. lengths preceeeding those.
id_ar = np.ones(N, dtype=int)
id_ar[0] = 0
insert_index = sizes[r1[:-1]].cumsum()
insert_val = (1-sizes)[r1[:-1]]

# 2. For each group, make sure the indexing starts from the next group's
# first element. So, simply assign 1s there.
insert_val[r1[1:] != r1[:-1]] = 1

# Assign index-offseting values
id_ar[insert_index] = insert_val

# Finally index into input array for the group repeated o/p
out = a[id_ar.cumsum()]
