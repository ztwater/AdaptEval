  nrToProcess = len(list)
  for s in list:
    s.doStuff()
    nrToProcess -= 1
    if nrToProcess==0:  # this is the last one
      s.doSpecialStuff()
