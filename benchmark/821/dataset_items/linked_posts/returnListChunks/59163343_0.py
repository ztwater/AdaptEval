def chunks(g, n):
  """divide a generator 'g' into small chunks
  Yields:
    a chunk that has 'n' or less items
  """
  n = max(1, n)
  buff = []
  for item in g:
    buff.append(item)
    if len(buff) == n:
      yield buff
      buff = []
  if buff:
    yield buff
