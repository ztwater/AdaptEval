chunk_size = 4
for i in range(0, len(ints), chunk_size):
    chunk = ints[i:i+chunk_size]
    # process chunk of size <= chunk_size
