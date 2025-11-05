def update_keys(newd, dic, mapping):
  def upsingle(d,k,v):
    if k in mapping:
      d[mapping[k]] = v
    else:
      d[k] = v
  for ekey, evalue in dic.items():
    upsingle(newd, ekey, evalue)
    if type(evalue) is dict:
      update_keys(newd, evalue, mapping)
    if type(evalue) is list:
      upsingle(newd, ekey, [update_keys({}, i, mapping) for i in evalue])
  return newd
