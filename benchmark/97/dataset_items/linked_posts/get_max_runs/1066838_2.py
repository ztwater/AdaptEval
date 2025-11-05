def runs_of_ones_array(bits):
  # make sure all runs of ones are well-bounded
  bounded = numpy.hstack(([0], bits, [0]))
  # get 1 at run starts and -1 at run ends
  difs = numpy.diff(bounded)
  run_starts, = numpy.where(difs > 0)
  run_ends, = numpy.where(difs < 0)
  return run_ends - run_starts
