def slice_grouper(n, sequence):
   return [sequence[i:i+n] for i in range(0, len(sequence), n)]
