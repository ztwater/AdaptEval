def runs_of_ones_list(bits):
  return [sum(g) for b, g in itertools.groupby(bits) if b]
