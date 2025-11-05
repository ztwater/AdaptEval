def correlation(dataset, threshold = 0.3):
  c = dataset.corr().abs()
  s = c.unstack()
  so = s.sort_values(kind="quicksort")
  results = []
  for index, row in so.items():
    if index[0] != index[1] and row > threshold:
      results.append({index: row})
  return results
