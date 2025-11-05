def get_dict(d, kl):
  cur = d[kl[0]]
  return get_dict(cur, kl[1:]) if len(kl) > 1 else cur
