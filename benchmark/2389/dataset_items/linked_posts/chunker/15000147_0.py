data = [...]
chunk_size = 10000 # or whatever
chunks = [data[i:i+chunk_size] for i in xrange(0,len(data),chunk_size)]
for chunk in chunks:
    ...
