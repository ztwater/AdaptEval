def runs_of_ones(bits):
  for bit, group in itertools.groupby(bits):
    if bit: yield sum(group)
