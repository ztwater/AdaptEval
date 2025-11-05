# Given 'l' is your list

chs = 12 # Your chunksize
partitioned = [ l[i*chs:(i*chs)+chs] for i in range((len(l) // chs)+1) ]
