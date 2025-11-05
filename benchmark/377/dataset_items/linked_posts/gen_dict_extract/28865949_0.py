def keyHole(k2b,o):
  # print "Checking for %s in "%k2b,o
  if isinstance(o, dict):
    for k, v in o.iteritems():
      if k == k2b and not hasattr(v, '__iter__'): yield v
      else:
        for r in  keyHole(k2b,v): yield r
  elif hasattr(o, '__iter__'):
    for r in [ keyHole(k2b,i) for i in o ]:
      for r2 in r: yield r2
  return
