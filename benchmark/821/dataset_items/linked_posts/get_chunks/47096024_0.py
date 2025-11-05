def chunks(iterable, chunk_size):
  i = 0;
  while i < len(iterable):
    yield iterable[i:i+chunk_size]
    i += chunk_size
